from django import template

from blog.models import Category

register = template.Library()


@register.simple_tag(name='get_list_ctg')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('blog/list_ctg.html')
def show_categories(arg1='Hello,', arg2=' Max'):
    categories = Category.objects.all()
    return {'categories': categories, 'arg1': arg1, 'arg2': arg2}
