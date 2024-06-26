from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order
from django.utils import timezone
from django.db.models import Q
from .forms import OrderForm
from .forms import ProductForm

# Create your views here.

# Create
def create_client(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        return redirect('client_list')
    return render(request, 'myapp/create_client.html')

# Read
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'myapp/client_list.html', {'clients': clients})

# Update
def update_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        client.name = request.POST.get('name')
        client.email = request.POST.get('email')
        client.phone_number = request.POST.get('phone_number')
        client.address = request.POST.get('address')
        client.save()
        return redirect('client_list')
    return render(request, 'myapp/update_client.html', {'client': client})

# Delete
def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        client.delete()
        return redirect('client_list')
    return render(request, 'myapp/delete_client.html', {'client': client})

# Product list
from django.utils import timezone

def client_product_list(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    now = timezone.now()
    week_ago = now - timezone.timedelta(days=7)
    month_ago = now - timezone.timedelta(days=30)
    year_ago = now - timezone.timedelta(days=365)

    products_7_days = Product.objects.filter(order__client=client, order__order_date__gte=week_ago).distinct()
    products_30_days = Product.objects.filter(order__client=client, order__order_date__gte=month_ago).distinct()
    products_365_days = Product.objects.filter(order__client=client, order__order_date__gte=year_ago).distinct()

    return render(request, 'myapp/client_product_list.html', {
        'client': client,
        'products_7_days': products_7_days,
        'products_30_days': products_30_days,
        'products_365_days': products_365_days,
    })

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            form.save_m2m()  # Save the many-to-many relationships
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'myapp/create_order.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'myapp/order_list.html', {'orders': orders})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'myapp/create_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})
