from django.db.models import Avg, F, DecimalField

from ..models import *


def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """
    result = OrderItem.objects.filter(
        order__date_formation__range=(begin, end)
    ).exclude(
        product__name=product
    ).aggregate(
        order_avg=Avg(F('product__product_costs__value') * F('count'))
    )
    print(result)
    if result.get('order_avg') is None:
        return 0

    return result
