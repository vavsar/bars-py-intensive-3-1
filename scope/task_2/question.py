"""
Что будет выведено после выполнения кода? Почему?
Будет выведено "Test message" и None
При вызове print(transmit_to_space("Test message")) внуть функции transmit_to_space передается текст.
Внутри функции сначала определяется, а затем и вызывается другая функция, которая пытается вывести значение
переменной message. Data_transmitter не находит message внутри локальной области видимости и идет на уровень выше,
где уже находит текст, переданный в функцию извне, его и выводит наружу.
А None выводится потому, что функция transmit_to_space ничего не возвращает явным образом, а по умолчанию идет
возврат None.
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))
