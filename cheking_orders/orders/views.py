from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import (Orders_vendor,
                     Orders_market,
                     Return_order,
                     Orders_on_claim,
                     Csv
                     )
from django.shortcuts import get_object_or_404, redirect
from cheking_orders.settings import MONTHS, YEARS
from .forms import (Orders_marketForm,
                    Orders_vendorForm,
                    Orders_on_claimForm,
                    Return_orderForm,
                    CsvForm
                    )
import csv


def month_status(month, year):
    orders = Orders_vendor.objects.filter(
        year_of_order=year,
        month_of_order=month)
    status_all = []
    for i in orders:
        status = i.order_status()
        if status not in status_all:
            status_all.append(status)

    return status_all


def index(request):
    template = 'orders/index.html'
    return render(request, template)


def years_list(request):
    template = 'orders/years_list.html'
    context = {
        'years': YEARS,
    }
    return render(request, template, context)


def months_list(request, year):
    template = 'orders/months_list.html'
    for month in MONTHS:
        status = month_status(month, year)

    context = {
        'status': status,
        'months': MONTHS,
        'year': year,
    }
    return render(request, template, context)


def month_list_orders(request, year, month):
    template = 'orders/month_list_orders.html'
    orders = Orders_vendor.objects.filter(
        year_of_order=year,
        month_of_order=month)
    context = {
        'orders': orders,
    }
    return render(request, template, context)


def upload(request):
    template = 'orders/upload.html'
    return render(request, template)


def upload_vendor(request):
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                row = ''.join(row)
                row = row.replace(';', ' ')
                row = row.split()
                order = int(row[0])
                month_of_order = int(row[1])
                year_of_order = int(row[2])
                sale_price = float(row[3])
                shipping_price = float(row[4])
                Orders_vendor.objects.get_or_create(
                    order=order,
                    month_of_order=month_of_order,
                    year_of_order=year_of_order,
                    sale_price=sale_price,
                    shipping_price=shipping_price,
                    )
        obj.activated = True
        obj.save()
    template = 'orders/uploadvendor.html'
    return render(request, template, {'form': form})


def upload_market(request):
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                row = ''.join(row)
                row = row.replace(';', ' ')
                row = row.split()
                order = int(row[0])
                month_of_order_market = int(row[1])
                year_of_order_market = int(row[2])
                sale_price_market = float(row[3])
                shipping_price_market = float(row[4])
                Orders_market.objects.get_or_create(
                    order=order,
                    month_of_order_market=month_of_order_market,
                    year_of_order_market=year_of_order_market,
                    sale_price_market=sale_price_market,
                    shipping_price_market=shipping_price_market,
                    )
        obj.activated = True
        obj.save()
    template = 'orders/uploadmarket.html'
    return render(request, template, {'form': form})


def upload_return(request):
    template = 'orders/upload.html'
    return render(request, template)


def upload_claim(request):
    template = 'orders/upload.html'
    return render(request, template)


def download(request):
    pass
