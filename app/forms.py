from django import forms
from .models import Product, Category

class SearchForm(forms.Form):
    query = forms.CharField(
        label='検索キーワード',
        max_length=100,  # CharField で max_length が有効です
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '検索したいキーワ ードを入力'}),
        # favorite = forms.BooleanField(label="check",required = False)
    )
    category = forms.ModelChoiceField(
        queryset = Category.objects.all(),
        label="Category",
        empty_label="選択してください",
        required=False
    )
    lower_damage = forms.IntegerField(
        label="最低ダメージ",
        required=False,
    )
    higher_damage = forms.IntegerField(
        label="最高ダメージ",
        required=False,
    )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'max_damage', 'category']
