from wishlist.models import Wishlist


def get_user_wishlists(request):
    if request.user.is_authenticated:
        return Wishlist.objects.filter(user=request.user).select_related('product')
    
    if not request.session.session_key:
        request.session.create()
    return Wishlist.objects.filter(session_key=request.session.session_key).select_related('product')