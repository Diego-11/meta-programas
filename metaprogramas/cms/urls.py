from django.urls import path
from cms import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
]
