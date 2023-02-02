from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from concessionaire.views import *

router = routers.DefaultRouter()
router.register('business',Business_view,basename='business')
router.register('inventory',Inventory_view,basename='inventory')
router.register('promotion',Promotion_view,basename='promotion')


router.register('employee',Employee_view,basename='employee')
router.register('automobile',Automobile_view,basename='automobile')
router.register('automobile_brand',Automobile_brand_view,basename='automobile_brand')
router.register('home',Home_view,basename='home')
router.register('user_interface',User_interface_view,basename='user_interface')
router.register('comparasion_automobile',Comparison_automobile_view,basename='Comparison_automobile_view')

urlpatterns = [
    path('', include(router.urls)),
    path('token', TokenProvider.as_view(), name='token'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)