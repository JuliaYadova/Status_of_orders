from django.db import models


class Orders_vendor(models.Model):
    """Данная модель хранит заказы по версии поставщика"""
    order = models.BigIntegerField(
        primary_key=True,
        verbose_name='Номер заказа')
    # Необходима проверка на мин и макс значения
    month_of_order = models.IntegerField(
        verbose_name='Месяц'
    )
    # Необходима проверка на мин и макс значения
    year_of_order = models.IntegerField(
        verbose_name='Год'
    )
    sale_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='РРЦ вендор')
    shipping_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Отгрузка вендор')

    def order_status(self):
        # Проверяем статус заказа
        if Orders_on_claim.objects.filter(
                    order__exact=self.order).exists():
            status_order = 'Учтено в претензии'
            return status_order
        elif Return_order.objects.filter(
                    order__exact=self.order).exists():
            status_order = 'Есть возврат'
            return status_order
        elif Orders_market.objects.filter(
                    order__exact=self.order).exists():
            status_order = 'Учтено в маркетплейсе'
            return status_order
        else:
            status_order = 'Не учтено в маркетплейсе'
            return status_order

    def order_summ(self):
        # Проверяем расхождения в цене
        market_order = Orders_market.objects.filter(order__exact=self.order)
        vendor_sp = self.sale_price
        vendor_shp = self.shipping_price
        market_sp = market_order.sale_price_market
        market_shp = market_sp - market_order.shipping_price_market
        sp_result = vendor_sp - market_sp
        shp_result = vendor_shp - market_shp
        if sp_result and shp_result != 0:
            price_status = 'Есть расхождения в цене'
            return price_status
        price_status = 'Нет расхождений в цене'
        return price_status


class Orders_market(models.Model):
    """Данная модель хранит заказы по версии маркетплейс"""
    order = models.ForeignKey(Orders_vendor, on_delete=models.CASCADE)
    sale_price_market = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='РРЦ маркетплейс')
    shipping_price_market = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Отгрузка маркетплейс')
    # Необходима проверка на мин и макс значения
    month_of_order_market = models.IntegerField(
        verbose_name='Месяц маркетплейс'
    )
    # Необходима проверка на мин и макс значения
    year_of_order_market = models.IntegerField(
        verbose_name='Год маркетплейс'
    )


class Return_order(models.Model):
    """Данная модель хранит заказы попавшие в возвраты"""
    """в документах маркетплейса."""
    order = models.ForeignKey(Orders_vendor, on_delete=models.CASCADE)
    month_of_return = models.IntegerField(
        verbose_name='Месяц в документах которого маркетплейс учел возврат'
    )
    # Необходима проверка на отрицательное число
    sale_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Сумма возврата итого по заказу')


class Orders_on_claim(models.Model):
    """Данная модель хранит заказы возмещенные маркетплейсом."""
    order = models.ForeignKey(Orders_vendor, on_delete=models.CASCADE)
    was_paid_for_return = models.BooleanField(
        verbose_name='Возврат в претензии')
    date_of_claim = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата претензии')


class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File id: {self.id}'
