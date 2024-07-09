from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/", views.getusers, name="getusers"),
    #get user/1
    path("user/<int:user_id>", views.getuserbyid, name="GetUserById"),
]