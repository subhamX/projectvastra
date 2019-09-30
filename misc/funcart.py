from cart.models import CartItem

def getcartc(user):
    cart_items = CartItem.objects.filter(user=user, bought=False)
    data = 0
    for item in cart_items:
        data += item.quantity
    return data