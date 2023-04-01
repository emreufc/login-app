from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("index", views.index, name="home"),
    path("product/<slug:slug>", views.product_details, name="product-details"),
    path("product/<slug:slug>", views.winnings, name="winnings"),
]
