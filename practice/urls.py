from django.urls import path
from .views import registerpage, homepage
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('', registerpage, name='register'),
    path('home', homepage, name='home'),
    path('login/', LoginView.as_view(template_name='practice/login.html'), name='login')
]