from django.http import HttpResponse
from django.shortcuts import redirect, render
from auction.models import Product

# Create your views here.

data = {
    "products":[
    {
        "id":1,
        "title": "SeventySeven Guitars Japan Tune-up Serisi EXRUBATO-STD/S JT AR",
        "image": "1.jpg",
        "description": "1.bilgi",
        "firstprice": 3000
    },
    {
        "id":2,
        "title": "Orville Orville Les Paul Standard Tiger Burst Les-Paul Standard 1993 Fujigen",
        "image": "2.jpg",
        "description": "2.bilgi",
        "firstprice": 5000
    },
    {
        "id":3,
        "title": "Martin/Martin OOO-28EC/000-28EC Eric Clapton",
        "image": "3.jpg",
        "description": "3.bilgi",
        "firstprice": 7000
    },
    ]
}

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {
        "products": Product.objects.all()
    }
    return render(request, "auction/index.html", context)

def product_details(request, slug):
    if not request.user.is_authenticated:
        return redirect("login")
    product = Product.objects.get(slug=slug)
    return render(request, "auction/product-details.html", {
        "product": product
    })
