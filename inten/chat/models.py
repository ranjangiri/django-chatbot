
from django.db import models
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_category():
        return Category.objects.all()

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    stipeend = models.IntegerField(default=0)
    des = models.CharField(max_length=100, default="")


    @staticmethod
    def get_all_products():
        return Item.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Item.objects.filter(category=category_id)
        else:
            return Item.get_all_products()

# Create your models here.


# Creating ChatBot Instance
