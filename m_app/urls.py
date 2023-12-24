from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EventViewSet, user_login
from .views import get_csrf_token

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
# router.register(r'users/login/', login, basename='user_login')

router.register(r'events', EventViewSet, basename='events')



urlpatterns = [
    path('users/login/', user_login, name='login'),
    path('', include(router.urls)),
    
]