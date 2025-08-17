from django.urls import path
from .views import home,products,profile,login,post

urlpatterns=[
    path('home/',home, name='home'),
    path('products/',products,name='products'),
    path('profile/',profile,name='profile'),
    path('login/',login,name='login'),
    path('post/',post,name='post'),
    
]