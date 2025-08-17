from django.shortcuts import render,redirect
from products.models import Product
from products.forms import ProductForm
from django.contrib.auth.decorators import login_required
import requests
from requests.exceptions import RequestException
from django.http import JsonResponse, HttpResponse

def post(request):
    try:
        response=requests.get('https://jsonplaceholder.typicode.com/posts/1')
        response.raise_for_status()
        return JsonResponse(response.json())
    except RequestException as e:
        # Log the error in a real application

        #Return a 503 Service Unavailable response
        return HttpResponse("Service unavailable", status=503)






@login_required
def profile(request):
    return render(request,'profile.html')

def login(request):
    return render(request,'login.html')


# Create your views here.
def home(request):
    return render(request,'index.html')

def products(request):
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            context={
                'products':Product.objects.all(),
                'form' : form
            }
    products=Product.objects.all()
    context={'products':products,'form':ProductForm()}
    return render(request, 'products.html',context)

