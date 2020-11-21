from django.shortcuts import render
from django.shortcuts import render
from .models import Item,Category


def index(request):
    obj = Item.objects.all()
    category = Category.get_all_category()
    a = request.GET.get('category')
    b=request.GET.get('details')
    result=None
    if a:
       obj = Item.get_all_products_by_id(a)

    else:
        obj= Item.get_all_products()
    data={}
    data['obj'] = obj
    data['category'] = category
    data['result']=b

    return render(request,'index.html',data)

# Create your views here.
