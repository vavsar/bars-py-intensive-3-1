from django.http import HttpResponse


OPERATORS = {
    '+': (lambda operand_1, operand_2: operand_1 + operand_2),
    '-': (lambda operand_1, operand_2: operand_1 - operand_2),
    '*': (lambda operand_1, operand_2: operand_1 * operand_2),
    '/': (lambda operand_1, operand_2: operand_1 / operand_2),
}


def calc(request):
    """
    Представление которому в параметре запроса maths через разделитель перечисляются простейшие арифметические операции
    например maths=3*3,10-2,10/5
    по умолчанию в качестве символа разделителя выступает сивол запятой.
    В необязательном параметре delimiter указывается символ разделителя арифметических операций
    например calc/?maths=3*3;10-2;10/5&delimiter=;

    Результат:  JsonResponse вида {'3*3': 9, '10-2': 8, '10/5': 2}
    """
    delimiter = request.GET.get('delimiter')
    maths = request.GET.get('maths').split(delimiter)
    result = []

    for calculation in maths:
        for operand in calculation:
            if operand in OPERATORS:
                number1, number2 = calculation.split(operand)
                operation = OPERATORS[operand](int(number1), int(number2))
                result.append(f'<p>{calculation} = {operation}</p>')

    return HttpResponse(result)
