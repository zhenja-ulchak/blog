from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<slug>/", views.post, name="post"),
    path("post_cart" ,views.blog_api, name="cart" ),
    path("info_api" ,views.info_api, name="info" )
    
]