from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . models import product,Contact
from math import ceil
# Create your views here.

def index(request):
    # return HttpResponse("Shop home of prince")
    # products = product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil(n/4 - n//4)
    # print(nSlides)
    # params = {"no_of_slides":nSlides, 'range':range(1,nSlides), 'product':products}

    # allProds = [[products,range(1,nSlides),nSlides],     #creating real data category wise insted of dummy data
    #               [products,range(1,nSlides),nSlides],
    #               [products,range(1,nSlides),nSlides]]

    allProds = []
    catprods = product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category = cat)
        n = len(prod)
        nSlide = n//4 + ceil(n/4 - n//4)
        allProds.append([prod,range(1,nSlide),nSlide])
    params = {"allProds":allProds}

    return render(request , 'shop/index.html',params)

def about(request):
    # return HttpResponse("About Page")
    return render(request , "shop/about.html" )

def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        phone = request.POST.get('contact')
        text = request.POST.get('text')
        name = request.POST.get('name')
        print(email, name, text, phone)

        contact_data = Contact(name=name, email=email, phone=phone, querry=text)
        contact_data.save()
    return render(request, "shop/contact.html")

def tracker(request):
    # return HttpResponse("Tracker page of our Shopping app")
    return render(request,"shop/tracker.html")

def search(request):
    return HttpResponse("This is our search page")

def productview(request,myid):
    # return HttpResponse("productview page of our shopping app")
    # product1 = get_object_or_404(product, id=myid)    
    product1 = product.objects.get(id = myid)
    print(product1)
    return render(request,"shop/productview.html",{"product":product1})

def checkout(request):
    return HttpResponse("Checkout page")

def cart(request):
    return HttpResponse("this is our cart page")

def order(request):
    return HttpResponse("ORDER PAGE OF SHOPPING APP")

def ex3(request):
    data = product.objects.all()
    return render(request,"shop/ex3.html",{'data': data})

