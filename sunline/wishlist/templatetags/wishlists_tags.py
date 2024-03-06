from django import template


from wishlist.models import Wishlist
from wishlist.utils import get_user_wishlists


register = template.Library()


@register.simple_tag()
def user_wishlists(request):
    # if request.user.is_authenticated:
    return get_user_wishlists(request)