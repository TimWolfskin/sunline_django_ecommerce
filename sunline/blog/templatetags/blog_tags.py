from django import template
from django.utils.http import urlencode


from blog.models import Category

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Category.objects.all()


