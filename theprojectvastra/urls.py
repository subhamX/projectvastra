from django.contrib import admin
from django.urls import path, include
from seller import urls as sellerUrls
from customer import urls as customerUrls
from accounts import urls as accountsUrls
from products import urls as productsUrls
from payments import urls as paymentsUrls
from cart import urls as cartUrls
from django.conf.urls.static import static
from django.conf import settings
from theprojectvastra import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', include(customerUrls)),
    path('admin/', admin.site.urls),
    path('seller/', include(sellerUrls)),
    path('accounts/', include(accountsUrls)),
    path('cart/', include(cartUrls)),
    path('payments/', include(paymentsUrls)),
    path('products/', include(productsUrls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.errorHandler
handler500 = views.errorHandler