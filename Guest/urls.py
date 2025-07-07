from django.urls import path
from Guest import views

app_name="Guest"
urlpatterns = [
    path('', views.index, name='index'),
    path('user_register/', views.user_register, name='user_register'),
    path('login/', views.login, name='login'),
]