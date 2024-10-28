from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm, UpdateUserInfo

def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UpdateUserInfo(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات کاربری شما ویرایش شد')
            return redirect("home")
        return render(request, "update_info.html", {'form':form})
    else:
        messages.success(request, 'ابتدا وارد پنل کاربری شوید')
        return redirect("home")

# Create your views here.
def category_summary(request):
    all_category = Category.objects.all()
    return render(request, 'category_summary.html', {'category':all_category})

def Home_Page(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products': all_products})

def About(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("با موفقیت وارد شدید"))
            return redirect("home")
        else:
            messages.success(request, ("نام کاربری یا گذرواژه اشتباه است"))
            return redirect("login")
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("با موفقیت خارج شدید!"))
    return redirect("home")

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, 'پروفایل شما ویرایش شد')
            return redirect("home")
        return render(request, "update_user.html", {'form':form})
    else:
        messages.success(request, 'ابتدا وارد پنل کاربری شوید')
        return redirect("home")
    
def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        
        if request.method == 'POST':
            form = UpdatePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "پسورد با موفقیت ویرایش شد")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect("update_password")
        else:
            form = UpdatePasswordForm(current_user)
        return render(request, "update_password.html", {'form':form})
    else:
        messages.success(request, "ابتدا وارد پنل کاربری شوید")
        return redirect("home")
    
def signup_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, ('حساب شما ساخته شد'))
            return redirect("update_info")
        else:
            messages.success(request, ('خطایی هنگام ثبت نام رخ داده است'))
            return redirect("signup")
    else:
        return render(request, 'signup.html', {'form':form})
    
    
def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def category(request, cat):
    cat = cat.replace("-", " ")
    try:
        category = Category.objects.get(name = cat)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ('چنین دسته بندی وجود ندارد'))
        return redirect("home")