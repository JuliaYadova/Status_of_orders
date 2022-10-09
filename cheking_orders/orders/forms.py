from django import forms
from .models import (Orders_vendor,
                     Orders_market,
                     Return_order,
                     Orders_on_claim,
                     Csv
                     )


class Orders_vendorForm(forms.ModelForm):
    class Meta:
        model = Orders_vendor
        fields = ('order',
                  'month_of_order',
                  'year_of_order',
                  'sale_price',
                  'shipping_price')


class Orders_marketForm(forms.ModelForm):
    class Meta:
        model = Orders_market
        fields = ('order',
                  'sale_price_market',
                  'shipping_price_market',
                  'month_of_order_market',
                  'year_of_order_market')


class Return_orderForm(forms.ModelForm):
    class Meta:
        model = Return_order
        fields = ('order',
                  'month_of_return',
                  'sale_price',)


class Orders_on_claimForm(forms.ModelForm):
    class Meta:
        model = Orders_on_claim
        fields = ('order',
                  'was_paid_for_return',
                  'date_of_claim',)


class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)
