from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3) # Show 3 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})
    

def view_necklaces(request):
    """View to display only necklaces"""
    products = Product.objects.all().filter(category='Necklaces')
    paginator = Paginator(products, 3) # Show 3 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})
    
def view_pendants(request):
    """View to display only Pendants"""
    products = Product.objects.all().filter(category='Pendants')
    paginator = Paginator(products, 3) # Show 3 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})
    
def view_earrings(request):
    """View to display only Earrings"""
    products = Product.objects.all().filter(category='Earrings')
    paginator = Paginator(products, 3) # Show 3 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})
    
def view_bracelets(request):
    """View to display only Bracelets"""
    products = Product.objects.all().filter(category='Bracelets')
    paginator = Paginator(products, 3) # Show 3 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})   
    
def view_rings(request):
    """View to display only Rings"""
    products = Product.objects.all().filter(category='Rings')
    paginator = Paginator(products, 3) # Show 3 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})   


def view_sets(request):
    """View to display only Sets"""
    products = Product.objects.all().filter(category='Sets')
    paginator = Paginator(products, 3) # Show 3 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})       
    
    
def product_detail(request, pk):
    """
    Create a view that returns a single
    feature object based on the feature ID (pk) and
    render it to the product_detail.html template
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {'product': product})
    