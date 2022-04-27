from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('appuser', AppUserViewSet, basename='appuser')
router.register('user', UserViewSet)
router.register('product', ProductViewSet)
router.register('orderitem', OrderItemViewSet)
router.register('order', OrderViewSet)
router.register('cart', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('app_user/', AppUserList.as_view()),
    #path('app_user/<int:pk>/', AppUserDetails.as_view()),
]