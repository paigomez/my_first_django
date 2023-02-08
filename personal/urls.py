from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hobbies', views.hobbies, name="hobbies"),
    path('contact_me', views.contact_me, name="contact_me")
 

]