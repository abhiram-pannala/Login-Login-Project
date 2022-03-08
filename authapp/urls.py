from django.urls import path
from . import views


urlpatterns=[
    path('', views.registerUser, name='register'),
    path('index/', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('webseries/', views.webseries, name='webseries'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('faq/', views.faq, name='faq'),
    path('sports/', views.sports, name='sports'),
    path('contact/', views.contact, name='contact'),
    path('NANAoffical/', views.NANAoffical, name='NANAoffical'),

    
]