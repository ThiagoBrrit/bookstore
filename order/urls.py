

from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from order import viewsets


router = routers.SimpleRouter()
router.register(r'order', viewsets.OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]

