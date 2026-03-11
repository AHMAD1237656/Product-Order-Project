from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Order

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'cards': products})

def place_order(request):
    if request.method == 'POST':
        product_id = request.POST.get('card_id')
        product = get_object_or_404(Product, id=product_id)

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        message = request.POST.get('message')

        # ✅ Save order to database
        Order.objects.create(
            product=product,
            name=name,
            email=email,
            phone=phone,
            address=address,
            message=message
        )

        # ✅ Optional: Show success message
        messages.success(request, f"Order placed for {product.title} successfully!")

        # ✅ Redirect to home page
        return redirect('home')

    # ✅ If GET request, redirect to home
    return redirect('home')
