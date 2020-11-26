from django.urls import path
from polls import views

urlpatterns = [

    path('form/<int:pk>', views.poll_form, name="meta_form"),
]
