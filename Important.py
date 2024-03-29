# print(int_num + float_num)

# # оператор "+" заменяется на магический метод __add__, но здесь будет ошибка, т.к. у класса int нет возможности сложить int с float
# print(int_num.__add__(float_num))
# print(float_num.__radd__(int_num))  # а у класса float такая возможность есть.

# print(id())  # показывает номер объекта в памяти
# print(type())  # показывает к какому типу относится объект
# print(dir())  # показывает список атрибутов класса. Или после класса поставить точку типа str.
# print(dir())  # показывает список всех переменных в глобальной зоне видимости. Или если мы напишем эту строку в функции,
# то покажется список переменных в зоне функции

# new_tuple = (1, 2)
# print(new_tuple.__doc__)  # описание функции typle, с помощью которой можно создавать кортежи
# получить справку о любом методе или обо всем классе, если убрать метод.
# print(help(new_tuple.count))
# print(first_comment.__dict__)  # проверяет собственные методы объекта определённого класса.
# print(list.__subclasses__())  # посмотреть список подклассов
# help('calendar')  # Вот так можно посмотреть инфо по определённому модулю
# help('modules')  # Список всех доступных по-умолчанию модулей в пайтон


# Сравнение типов данных

# _______Изменения   Порядок Одинаковые элементы    Символ
# list      +           +       +                       []
# tuple     -           +       +                       ()
# set       +           -       -                       {}
# range     -           +       -                       ()
# dict      +           -       -                       {}
# str       -           +       +                       ''
# int       -
# float     -

# set - если нужно создать последовательность уникальных элементов
# dict - если нужно хранить большие объемы данных, у которых есть идентификатор (ключ)
# list - если нужна просто упорядоченная последовательность элементов, можно разных типов, элементы могут повторяться
# tuple - если нужен набор данных, в котором нельзя удалять элементы
# range - если нужно выполнить некоторые действия много раз

# Как они создаются:
# list == my_fruits = ['apple', 'orange', 'pineapple']
# tuple == new_tuple = (1, 3, 5, 'ile', True). Могут быть объекты разных классов
# set == my_fruits = {'apple', 'banana', 'orange'}
# range == my_range = range(10, 20, 3)
# str == my_comment = 'This is my long comment'
# dict == my_motorbyke = {
#     'name': 'Ducati',
#     'price': 25000,
#     'engine_vol': 1.2,
# }

# Соотнесение типов python и json:
# str = String
# int, float = Number
# True = true
# False = false
# None = null
# dict = Object
# list, tuple = Array
