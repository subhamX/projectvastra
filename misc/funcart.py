from cart.models import CartItem

def getcartc(user):
    return CartItem.objects.filter(user=user, bought=False).count()