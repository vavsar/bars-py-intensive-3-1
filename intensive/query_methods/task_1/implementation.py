from django.shortcuts import get_object_or_404

from ..models import *


def get_order_count_by_customer(name):
    """Возвращает количества заказов по имени покупателя

    Args:
        name: имя покупателя

    Returns: число заказов (не может быть отрицательным, но может быть нулевым)
    """
    try:
        customer = get_object_or_404(Customer, name=name)
        orders_count = customer.get_orders_count
    except:
        orders_count = 0

    return orders_count
