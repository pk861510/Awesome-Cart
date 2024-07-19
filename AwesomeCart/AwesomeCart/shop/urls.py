from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name = "Shop-home"),
    path("about",views.about,name = "Shop-about"),
    path("contact",views.contact,name = "Shop-contact"),
    path("tracker",views.tracker,name = "Shop-tracker"),
    path("search",views.search,name = "Shop-search"),
    path("prodview/<int:myid>",views.productview,name = "Shop-prodview"),
    path("checkout",views.checkout,name = "Shop-checkout"),
    path("cart/",views.cart,name = "Shop-cart"),
    path("order",views.order,name = "Shop-order"),
    path("ex3/",views.ex3 , name = "Ex3")
]