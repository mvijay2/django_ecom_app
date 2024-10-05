from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Category

# Create your views here.
#request -> response
#request handler
#data exchange
def category(request, foo):
    foo= foo.replace('-', ' ')
    #grab the category from the url
    try:
        category= Category.objects.get(name=foo)
        products= Product.objects.filter(category=category)
        return render(request, 'category.html',{'products':products, 'category':category})
    except:
        messages.success(request, ("not existed"))
        return redirect('hello')


def product(request,pk):
    product= Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})


def say_hello(request): #basically response we use to extract, transform, the database data
    products= Product.objects.all()
    return render(request, 'hello.html', {'products': products})
    
def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, ("you have been logged in"))
            return redirect('hello')
        else:
            messages.success(request, ("there was an error, try again"))  
            return render(request, 'login')
    else: 
        return render(request, 'login.html')



def logout_user(request):
    logout(request)
    messages.success(request, ("you have been successfully logout"))
    return redirect('hello')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            #login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("you have been successfully registered"))
            return redirect('hello')
        
        else:
            messages.success(request, ("there was an error,register again "))
            return redirect('register')



    else:
        return render(request, 'register.html', {'form':form})



