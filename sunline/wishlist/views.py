from django.shortcuts import render
from django.http import JsonResponse
from goods.models import Products
from wishlist.models import Wishlist
from django.template.loader import render_to_string
from wishlist.utils import get_user_wishlists



def wishlist_add(request):
    product_id = request.POST.get("product_id")

    product = Products.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        wishlists = Wishlist.objects.filter(user=request.user, product=product)

        if wishlists.exists():
            wishlist = wishlists.first()
            if wishlist:
                wishlist.quantity += 1
                wishlist.save()
        else:
            Wishlist.objects.create(user=request.user, product=product, quantity=1)

    else:
        wishlists = Wishlist.objects.filter(
            session_key=request.session.session_key, product=product)

        if wishlists.exists():
            wishlist = wishlists.first()
            if wishlist:
                wishlist.quantity += 1
                wishlist.save()
        else:
            Wishlist.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)
    
    user_wishlist = get_user_wishlists(request)
    wishlist_items_html = render_to_string(
        "wishlists/includes/included_wishlist.html", {"wishlists": user_wishlist}, request=request)

    response_data = {
        "message": "Product added to wishlist",
        "wishlist_items_html": wishlist_items_html,
    }

    return JsonResponse(response_data)




def remove_wishlist(request):
    wishlist_id = request.POST.get("wishlist_id")

    wishlist = Wishlist.objects.get(id=wishlist_id)
    quantity = wishlist.quantity
    wishlist.delete()

    user_wishlist = get_user_wishlists(request)
    wishlist_items_html = render_to_string(
        "wishlists/includes/included_wishlist.html", {"wishlists": user_wishlist}, request=request)

    response_data = {
        "message": "Product removed",
        "wishlist_items_html": wishlist_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)
