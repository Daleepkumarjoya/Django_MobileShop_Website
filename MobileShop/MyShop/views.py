from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, contact, Orders
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def HomePage(request):
    products = Product.objects.all()
    if request.method == 'GET':
        st = request.GET.get('productname')
        if st is not None:
            products = Product.objects.filter(Product_Name__icontains=st)
    ProdParams = {'products': products}
    return render(request, 'HomePage.html', ProdParams)


def ViewPage(request, id):
    product = Product.objects.filter(id=id)
    return render(request, 'ViewPage.html', {'product': product[0]})


def checkout(request, id):
    product = Product.objects.filter(id=id)
    if request.method == 'POST':
        # ItemJson = request.POST.get('ItemJson')
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        Address = request.POST.get('Address')
        if len(number) <= 0:
            messages.success(request, 'Please Enter Mobile Number.')
        else:
            Check = Orders(Name=name, Email=email, number=number, Address=Address)
            Check.save()
            messages.success(request, 'Your Order Has Been Submitting Successfully.')
    return render(request, 'checkOuts.html', {'product': product[0]})


def aboutPage(request):
    return render(request, 'aboutUs.html')


def contactUsPage(request):
    if request.method == 'POST':
        print(request)
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        query = request.POST.get('query')
        cont = contact(Name=name, Email=email, number=number, query=query)
        cont.save()
    return render(request, 'contactUs.html')


def registerPage(request):
    if request.method == 'POST':
        UserName = request.POST['Username']
        first_Name = request.POST['firstname']
        last_Name = request.POST['lstName']
        email = request.POST['email']
        Password = request.POST['password']
        CPassword = request.POST['Cpassword']
        if Password == CPassword:
            if User.objects.filter(username=UserName).exists():
                messages.success(request, 'User Name Has Been Taken.')
            elif User.objects.filter(email=email).exists():
                messages.success(request, 'Email Has Been Taken.')
            else:
                MyUser = User.objects.create_user(username=UserName, first_name=first_Name, last_name=last_Name,
                                                  email=email, password=Password)
                MyUser.save()
                messages.success(request, 'User Has Been Created.')
                return redirect('/logInPage/')
        else:
            messages.success(request, 'Password do not Match.')
        return redirect('/registerPage/')
    else:
        return render(request, 'Register.html')


def logInPage(request):
    if request.method == 'POST':
        UserName = request.POST['logUserName']
        Password = request.POST['logPassword']
        MyUser = auth.authenticate(username=UserName, password=Password)
        if MyUser is not None:
            auth.login(request, MyUser)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/logInPage/')
    else:
        return render(request, 'LogIn.html')


def logOutPage(request):
    auth.logout(request)
    return redirect('/')
