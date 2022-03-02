from django.db import (
    models,
)


class Product(models.Model):
    """
    Товар
    """
    name = models.CharField('Наименование', max_length=300)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class ProductCount(models.Model):
    """
    Количество товара
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    begin = models.DateField('Начало периода')
    end = models.DateField('Окончание периода')
    value = models.PositiveIntegerField('Значение')

    class Meta:
        db_table = 'product_count'


class ProductCost(models.Model):
    """
    Стоимость товара
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    begin = models.DateField('Начало периода')
    end = models.DateField('Окончание периода')
    value = models.DecimalField('Значение', max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'product_cost'


class Customer(models.Model):
    """
    Покупатель
    """
    name = models.CharField('Покупатель', max_length=300)

    @property
    def get_orders_count(self):
        if not self:
            return 0
        return self.orders.count()

    def get_orders_in_time_count(self, begin, end):
        if not self:
            return 0
        return self.orders.filter(date_formation__gte=begin, date_formation__lte=end).count()

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Заказ
    """
    number = models.CharField('Номер', max_length=50)
    date_formation = models.DateField('Дата')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='Покупатель', related_name='orders')

    class Meta:
        db_table = 'order'


class OrderItem(models.Model):
    """
    Позиция заказа
    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ', related_name='order_items')
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Товар', related_name='order_items')
    count = models.DecimalField(verbose_name='Количество', max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'order_item'
