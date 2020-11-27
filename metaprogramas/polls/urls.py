from django.urls import path
from polls import views
from polls.utils import pdf

urlpatterns = [

    path('form/<int:pk>', views.poll_form, name="meta_form"),
    path('result/<int:pk>', views.result, name="result"),

]
