from django.db.models import Sum, IntegerField

from ..models import *


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """
    result = OrderItem.objects.values_list('product__name').annotate(
        product_count=Sum('count', output_field=IntegerField())
    ).filter(
        order__date_formation__range=(begin, end)
    ).order_by('-product_count')
    if not result.exists():
        return []

    return [result[0]]
