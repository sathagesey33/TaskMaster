# urls.py
from django.urls import path
from .views import RegisterView, LoginView, LoginWithGoogle

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('google/login/', LoginWithGoogle.as_view(), name='login_with_google'),
]
