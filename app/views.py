from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Favorite
from .forms import ProductForm, SearchForm
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('app:product_list')
    else:
        form = ProductForm(instance=product) # product オブジェクトをテンプレートに渡す
    return render(request, 'product_form.html', {'form': form, 'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('app:product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

def product_list(request):
    form = SearchForm(request.GET or None)
    products = Product.objects.all()
    favorites = [c.favorite_product for c in Favorite.objects.filter(favorite_user = request.user.id)]
    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            products = products.filter(name__icontains=query) # カテゴリフィルタリング
        category = form.cleaned_data['category']
        if category:
            products = products.filter(category = category)
        higher_damage = form.cleaned_data['higher_damage']
        if higher_damage:
            products = products.filter(max_damage__lte = higher_damage)
        lower_damage = form.cleaned_data['lower_damage']
        if lower_damage:
            products = products.filter(max_damage__gte = lower_damage)
        favorite_only = form.cleaned_data['favorite_only']
        if favorite_only:
            products = [c.favorite_product for c in Favorite.objects.filter(favorite_user = request.user.id)]

    # format_products = []
    # for c in products:
    #     favorited_dict = {"favorited": c in favorites}
    #     new_dict = {**c.__dict__, **favorited_dict}
    #     format_products.append(new_dict)
    #     # print(dict(c))
    # print(format_products)
    # # print(list(favorites)[0])
    # # Favorite.objects.filter(favorite_user = request.user)
    return render(request, 'product_list.html', {'products': products, 'favorites': favorites, 'form': form})

def search_view(request):
    form = SearchForm(request.GET or None)
    results = Product.objects.all() # クエリセットの初期化 if form.is_valid():
    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            results = results.filter(name__icontains=query) # カテゴリフィルタリング

    category_name = request.GET.get('category')
    if category_name:
        try:
            # カテゴリ名に基づいてカテゴリ ID を取得
            category = Category.objects.get(name=category_name) 
            results = results.filter(category_id=category.id)
        except Category.DoesNotExist:
            results = results.none() # 存在しないカテゴリの場合、結果を空にする 
            category = None
    # 価格のフィルタリング(最低価格・最高価格) 
    min_price = request.GET.get('min_price') 
    max_price = request.GET.get('max_price')

    if min_price:
        results = results.filter(price__gte=min_price)
    if max_price:
        results = results.filter(price__lte=max_price)
    # 並び替え処理
    sort_by = request.GET.get('sort', 'name') 
    if sort_by == 'price_asc':
            results = results.order_by('max_damage')
    elif sort_by == 'price_desc':
        results = results.order_by('-max_damage')
    # クエリセットをリストに変換せず、直接 Paginator に渡す 
    paginator = Paginator(results, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search.html', {'form': form, 'page_obj': page_obj, 'results': results})

@login_required
def Favorite_page(request: HttpRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    favorite_objects = Favorite.objects.filter(favorite_product = product, favorite_user = request.user)
    if favorite_objects.exists():
        favorite_objects.delete()
    else:
        request_user = request.user
        fp = Favorite(
            favorite_product=product,
            favorite_user=request_user,
        )
        fp.save()
    return redirect('app:product_list')

def Product_description(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_description.html', {'product': product})