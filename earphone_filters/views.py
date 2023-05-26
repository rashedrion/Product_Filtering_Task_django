from django.shortcuts import render
from .models import Earphone
from .forms import EarphoneFilterForm

from django.shortcuts import render, get_object_or_404


def earphone_detail(request, pk):
    earphone = get_object_or_404(Earphone, pk=pk)
    return render(request, 'earphone_detail.html', {'earphone': earphone})


def earphone_list(request):
    form = EarphoneFilterForm(request.GET)
    earphones = Earphone.objects.all()

    if form.is_valid():
        min_price = form.cleaned_data['min_price']
        max_price = form.cleaned_data['max_price']
        brand = form.cleaned_data['brand']
        product_type = form.cleaned_data['product_type']
        seller = form.cleaned_data['seller']
        product_name = form.cleaned_data['product_name']
        min_warranty = form.cleaned_data['min_warranty']
        max_warranty = form.cleaned_data['max_warranty']

        if min_price:
            earphones = earphones.filter(price__gte=min_price)
        if max_price:
            earphones = earphones.filter(price__lte=max_price)
        if brand:
            earphones = earphones.filter(brand=brand)
        if product_type:
            earphones = earphones.filter(product_type=product_type)
        if seller:
            earphones = earphones.filter(seller=seller)
        if product_name:
            earphones = earphones.filter(name__icontains=product_name)
        if min_warranty:
            earphones = earphones.filter(warranty_period__gte=min_warranty)
        if max_warranty:
            earphones = earphones.filter(warranty_period__lte=max_warranty)

    return render(request, 'earphone_list.html', {'earphones': earphones, 'form': form})
