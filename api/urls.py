from rest_framework import routers
from api.views import *
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
router  = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('user', UserViewSet)
router.register('categoria', CategoriasViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
  

] + router.urls