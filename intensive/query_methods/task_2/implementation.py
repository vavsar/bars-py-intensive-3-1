from django.db.models import Count, Q

from ..models import *


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    between_dates = Count('orders', filter=Q(orders__date_formation__gte=begin) & Q(orders__date_formation__lte=end))
    customer = Customer.objects.filter(
        orders__date_formation__gte=begin, orders__date_formation__lte=end
    ).annotate(
        orders_count=between_dates
    ).order_by(
        '-orders_count', 'orders__date_formation', 'name'
    ).first()
    if customer is not None:
        output = (customer.name, customer.get_orders_in_time_count(begin, end))
    else:
        output = None

    return output
