from django.urls import path
from User import views


app_name="User"
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),

]





