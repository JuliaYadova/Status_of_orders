from django.contrib import admin
from .models import (Csv,
                     Orders_market,
                     Orders_vendor,
                     Orders_on_claim,
                     Return_order
                     )

admin.site.register(Csv)


class Orders_vendorAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'month_of_order',
        'year_of_order',
    )
    search_fields = ('order',)
    list_filter = ('year_of_order', 'month_of_order')
    empty_value_display = '-пусто-'


admin.site.register(Orders_vendor, Orders_vendorAdmin)


class Orders_marketAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'month_of_order_market',
        'year_of_order_market',
    )
    search_fields = ('order',)
    list_filter = ('year_of_order_market', 'month_of_order_market')
    empty_value_display = '-пусто-'


admin.site.register(Orders_market, Orders_marketAdmin)


class Orders_on_claimAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'date_of_claim',
    )
    search_fields = ('order',)
    list_filter = ('date_of_claim',)
    empty_value_display = '-пусто-'


admin.site.register(Orders_on_claim, Orders_on_claimAdmin)


class Return_orderAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'month_of_return',
    )
    search_fields = ('order',)
    list_filter = ('month_of_return',)
    empty_value_display = '-пусто-'


admin.site.register(Return_order, Return_orderAdmin)
