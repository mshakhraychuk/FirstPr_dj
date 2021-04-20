from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Category


def index(request):
    blog = Blog.objects.all
    context = {
        'blog': blog,
        'title': 'Список статей',
    }
    return render(request, 'blog/index.html', context)


def get_category(request, category_id):
    blog = Blog.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'blog/category.html', {"blog": blog, 'category': category})
