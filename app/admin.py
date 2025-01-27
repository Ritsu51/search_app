from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Category, Favorite


from .models import Product
# Register your models here

admin.site.register(Product)
admin.site.register(Favorite)
# admin.site.register(Category)
admin.site.unregister(Group)