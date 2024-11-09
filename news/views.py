from django.shortcuts import render
from .models import Category , News ,Social
from django.views import View
# Create your views here.

class MainView(View):
    def get(self , request):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'index.html', context=context)
class CategoryView(View):
    def get(self, request, id):
       category = Category.objects.get(id=id)
       news = category.category_news.all().order_by('-create_date')[:20]
       context = {
           'news':news,
           'category_name' : category.name,
       }
       return render(request, template_name='category.html', context=context)

