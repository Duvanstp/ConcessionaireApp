from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from concessionaire.views import *

router = routers.DefaultRouter()
router.register('business',Business_view,basename='business')
router.register('employee',Employee_view,basename='employee')
router.register('automobile',Automobile_view,basename='automobile')
router.register('inventory',Inventory_view,basename='inventory')
router.register('promotion',Promotion_view,basename='promotion')

urlpatterns = [
    path('', include(router.urls)),
    path('token', TokenProvider.as_view(), name='token'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)