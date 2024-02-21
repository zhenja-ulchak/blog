from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name= "logout"),
    path("password_change/", views.password_change, name= "password_change"),

]