from django import template
from news.models import Cat
from django.db.models import Count
from news.utils import menu_header

register = template.Library()

@register.simple_tag()
def get_cat():
    cat = Cat.objects.annotate(total = Count('posts'))
    return cat

@register.simple_tag()
def get_menu():
    return menu_header
