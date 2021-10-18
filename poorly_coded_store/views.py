from django.shortcuts import render,redirect 
from .models import Order, Product

def index(request):
    if request.method=="GET":
        context = {
            "all_products": Product.objects.all()
        }
        return render(request, "store/index.html", context)
    elif request.method== "POST":
        quantity_from_form = int(request.POST["quantity"])
        product_id= request.POST["product_id"]
        price_from_form = Product.objects.get(id=product_id).price
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        return redirect("/checkout")

def checkout(request):
    context={
    "last_order": Order.objects.last()
}
    return render(request, "store/checkout.html",context)