from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    max_damage = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) # 1はカテゴリID

    def __str__(self):
        return self.name

class Favorite(models.Model):
    favorite_product = models.ForeignKey('Product', on_delete=models.CASCADE)
    favorite_user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)