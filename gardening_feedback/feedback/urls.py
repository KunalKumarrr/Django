from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login_user'),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('thanks/', views.feedback_thanks, name='feedback_thanks'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register_user'),
]
