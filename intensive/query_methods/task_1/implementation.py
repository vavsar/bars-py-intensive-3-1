from django.shortcuts import get_object_or_404

from ..models import *


def get_order_count_by_customer(name):
    """Возвращает количества заказов по имени покупателя

    Args:
        name: имя покупателя

    Returns: число заказов (не может быть отрицательным, но может быть нулевым)
    """
    try:
        customer = Customer.objects.get(name=name)
        orders_count = customer.orders_count
    except Customer.DoesNotExist:
        return 0
    except Customer.MultipleObjectsReturned:
        return 0

    return orders_count
