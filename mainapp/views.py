from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')

def product(request, product_id):
    return render(request, 'product.html', {'product_id': product_id})

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')
