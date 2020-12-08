from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from customers.forms.loginform import LoginForm
from customers.forms.profileform import CustomerProfileForm
from customers.forms.signupform import SignUpForm
from customers.models import Customer
from store.models import Order


def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    if request.method == 'GET':
        context = {
            'user': user,
            'profile': user.customer,
            'form': CustomerProfileForm(),
            'products': user.customer.product_set.all(),
            'cartItems': cartItems,
        }
        return render(request, 'customers/user_profile.html', context)
    else:
        form = CustomerProfileForm(request.POST, request.FILES, instance=user.customer)
        if form.is_valid():
            form.save()
            context = {
                'user': user,
                'profile': user.customer,
                'products': user.customer.product_set.all(),
                'form': form,
                'cartItems': cartItems,
            }
            return render(request, 'customers/user_profile.html', context)

        return redirect('/')


def signup_user(request):
    if request.method == 'GET':
        context = {
            'form': SignUpForm(),
        }
        return render(request, 'customers/signup.html', context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Customer(
                user=user,
            )
            profile.save()
            login(request, user)
            return redirect('/')
        context = {
            'form': form,
        }
        return render(request, 'customers/signup.html', context)


def login_user(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm()
        }
        return render(request, 'customers/login.html', context)
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
        context = {
            'form': form,
        }

        return render(request, 'customers/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')
