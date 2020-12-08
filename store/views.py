from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from .forms.productform import ProductForm
from .models import *

# Create your views here.


@login_required
def create_product(request):
    if request.method == 'GET':
        form = ProductForm()
        customer = request.user.customer
        user = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        context = {
            'form': form,
            'cartItems': cartItems,
            'user': user,
        }

        return render(request, 'store/create_product.html', context)
    else:

        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/')
        else:
            context = {
                'form': form,
            }
            return render(request, 'store/create_product.html', context)


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'product': product,
            'can_delete': request.user == product.user.user,
            'can_update': request.user == product.user.user,
         }

        return render(request, 'store/product_details.html', context)


@login_required
def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        context = {
            'form': form,
            'product': product,
        }
        return render(request, 'store/edit_product.html', context)
    else:
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/', product.pk)
        else:
            context = {
                'form': form,
                'product': product,
            }
            return render(request, 'store/edit_product.html', context)


@login_required
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'product': product,
        }
        return render(request, 'store/delete_product.html', context)
    else:
        product.delete()
        return redirect('/')


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    # Paginator
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'cartItems': cartItems,
        'page_obj': page_obj,
    }
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'customer': customer,
    }

    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def get_shoes(request):
    products = Product.objects.filter(category='Shoes')
    # Paginator
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {
        'products': products,
        'cartItems': cartItems,
        'page_obj': page_obj,
    }
    return render(request, 'store/shoes.html', context)
