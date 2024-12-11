from django.urls import path
from .views import register, user_login, CustomAuthToken

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', user_login, name='profile'),
    path('token/', CustomAuthToken.as_view(), name='token'),
]