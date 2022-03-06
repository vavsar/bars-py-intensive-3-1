from django.db.models import Count, Q

from ..models import *


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    between_dates = Count('orders', filter=Q(orders__date_formation__range=(begin, end)))
    customer = Customer.objects.filter(
        orders__date_formation__range=(begin, end)
    ).annotate(
        count_orders=between_dates
    ).order_by(
        '-count_orders', 'orders__date_formation', 'name'
    ).first()
    if customer is None:
        output = None
    else:
        output = (customer.name, customer.get_orders_in_period(begin=begin, end=end))

    return output
