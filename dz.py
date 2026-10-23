2. Линейный поиск (Linear Search) 

Линейный поиск — самый простой способ. Мы просто перебираем все элементы и проверяем каждый.

Алгоритм:

Берём первый элемент.
Если он равен искомому — нашли.
Если нет — берём следующий.
Повторяем, пока не найдём или не кончится список.
Пример:

python

def linear_search(arr, target):

    """

    Линейный поиск элемента в списке.

    Возвращает индекс элемента или -1, если не найден.

    """

    for i in range(len(arr)):

        if arr[i] == target:

            return i  # Нашли!

    return -1  # Не нашли

 

# Проверяем

numbers = [10, 25, 30, 45, 50, 65, 70]

target = 45

 

index = linear_search(numbers, target)

if index != -1:

    print(f"Элемент {target} найден на позиции {index}")

else:

    print(f"Элемент {target} не найден")

Когда использовать линейный поиск?

Когда список не отсортирован.
Когда список маленький (до 1000 элементов).
Когда нужно найти не по точному совпадению, а по частичному.
3. Бинарный поиск (Binary Search)

Бинарный поиск — гораздо быстрее, но работает ТОЛЬКО на ОТСОРТИРОВАННЫХ списках.

Алгоритм:

Найти средний элемент.
Если он равен искомому — нашли.
Если искомое меньше среднего — ищем в левой половине.
Если искомое больше среднего — ищем в правой половине.
Повторяем, пока не найдём или не останется элементов.
Визуализация:

text

Список: [1, 3, 5, 7, 9, 11, 13]

Ищем: 7

 

Шаг 1: средний = 7 (индекс 3) → 7 == 7 → НАШЛИ!

text

Ищем: 1

 

Шаг 1: средний = 7 → 1 < 7 → смотрим левую половину [1, 3, 5]

Шаг 2: средний = 3 → 1 < 3 → смотрим левую половину [1]

Шаг 3: средний = 1 → 1 == 1 → НАШЛИ!

Код:

python

def binary_search(arr, target):

    """

    Бинарный поиск. Список должен быть ОТСОРТИРОВАН!

    """

    left = 0

    right = len(arr) - 1

   

    while left <= right:

        mid = (left + right) // 2  # Средний индекс

       

        if arr[mid] == target:

            return mid  # Нашли!

        elif arr[mid] < target:

            left = mid + 1  # Ищем в правой половине

        else:

            right = mid - 1  # Ищем в левой половине

   

    return -1  # Не нашли

 

# Проверяем

numbers = [1, 3, 5, 7, 9, 11, 13]

print(binary_search(numbers, 7))  # 3

print(binary_search(numbers, 1))  # 0

print(binary_search(numbers, 10)) # -1

4. Сравнение линейного и бинарного поиска (20 минут)

Критерий

Линейный поиск

Бинарный поиск

Требования

Любой список

Только отсортированный

Скорость

O(n)

O(log n)

Найти в 1 000 000 элементов

До 1 000 000 шагов

~20 шагов

Сложность реализации

Простая

Сложнее

Наглядная разница:

python

import time

 

# Создаём список из 1 000 000 элементов

big_list = list(range(1_000_000))

target = 999_999

 

# Линейный поиск

start = time.time()

linear_search(big_list, target)

print(f"Линейный поиск: {time.time() - start:.4f} сек.")

 

# Бинарный поиск

start = time.time()

binary_search(big_list, target)

print(f"Бинарный поиск: {time.time() - start:.4f} сек.")

Ожидаемый результат:

text

Линейный поиск: 0.0345 сек.

Бинарный поиск: 0.0001 сек.

5. Поиск в словарях 

В Python поиск в словаре — это O(1) (мгновенный)!

python

users = {

    "alex": "Алексей",

    "maria": "Мария",

    "ivan": "Иван"

}

 

# Поиск по ключу

name = users.get("maria")

print(name)  # Мария

 

# Проверка наличия

if "ivan" in users:

    print("Пользователь есть!")

 

# Поиск по значению (медленнее)

for key, value in users.items():

    if value == "Мария":

        print(f"Мария — это {key}")

6. Поиск с частичным совпадением

Иногда нужно найти не точное совпадение, а похожее.

python

products = [

    {"name": "Наушники", "price": 500},

    {"name": "Беспроводные наушники", "price": 1500},

    {"name": "Телефон", "price": 30000},

    {"name": "Чехол для телефона", "price": 300},

]

 

# Поиск по части названия

search_query = "науш"

 

results = []

for product in products:

    if search_query.lower() in product["name"].lower():

        results.append(product)

 

print(f"Найдено товаров: {len(results)}")

for item in results:

    print(f"- {item['name']} ({item['price']} руб.)")

Результат:

text

Найдено товаров: 2

- Наушники (500 руб.)

- Беспроводные наушники (1500 руб.)

7. Использование модуля bisect

Python уже имеет встроенный бинарный поиск в модуле bisect.

python

import bisect

 

numbers = [1, 3, 5, 7, 9, 11, 13]

 

# Найти позицию, куда вставить число, чтобы сохранить сортировку

pos = bisect.bisect_left(numbers, 6)

print(pos)  # 3 (число 6 должно быть на позиции 3)

 

# Проверить, есть ли число

target = 7

pos = bisect.bisect_left(numbers, target)

if pos < len(numbers) and numbers[pos] == target:

    print(f"{target} найдено на позиции {pos}")

else:

    print(f"{target} не найдено")

8. Практический пример

Задача: Найти все товары дешевле 1000 рублей и отсортировать их по цене.

python

products = [

    {"name": "Наушники", "price": 500, "rating": 4.5},

    {"name": "Телефон", "price": 30000, "rating": 4.8},

    {"name": "Чехол", "price": 300, "rating": 3.5},

    {"name": "Зарядка", "price": 700, "rating": 4.2},

    {"name": "Плеер", "price": 2000, "rating": 4.0},

]

 

# 1. Фильтрация

cheap_products = [p for p in products if p["price"] < 1000]

 

# 2. Сортировка

sorted_cheap = sorted(cheap_products, key=lambda x: x["price"])

 

# 3. Вывод

print("Товары дешевле 1000 рублей:")

for p in sorted_cheap:

    print(f"- {p['name']}: {p['price']} руб.")

Результат:

text

Товары дешевле 1000 рублей:

- Чехол: 300 руб.

- Наушники: 500 руб.

- Зарядка: 700 руб.