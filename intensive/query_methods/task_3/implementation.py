from django.db.models import F, Sum, IntegerField, Max

from ..models import *


def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """

    result = OrderItem.objects.values_list(
        'order__number'
    ).annotate(
        order_cost=F('product__product_costs__value') * F('count')
    ).filter(
        order__date_formation__range=(begin, end)
    ).order_by('-order_cost', '-order__number')

    print(result.query)
    print('queryset: ', result)

    if result.exists():
        return result[0]
    else:
        return None
