class Product:  # Определение класса Product
    def __init__(self, name, weight, category):  # Определение конструктора класса с аргументами name, weight, category
        self.name = name  # Инициализация атрибута name
        self.weight = weight  # Инициализация атрибута weight
        self.category = category  # Инициализация атрибута category

    def __str__(self):  # Определение метода __str__ для строкового представления объекта
        return f'{self.name}, {self.weight}, {self.category}'  # Возвращение строки с атрибутами объекта


class Shop:  # Определение класса Shop
    def __init__(self):  # Определение конструктора класса
        self.file_name = 'products.txt'  # Инициализация атрибута file_name

    def get_products(self):  # Определение метода get_products для получения списка продуктов
        with open(self.file_name, 'r') as file:  # Открытие файла для чтения
            return file.read()  # Возвращение содержимого файла в виде строки

    def add(self, *products):  # Определение метода add для добавления продуктов
        existing_products = self.get_products().split('\n')  # Получение списка существующих продуктов из файла

        with open(self.file_name, 'a') as file:  # Открытие файла для дозаписи
            for product in products:  # Перебор переданных продуктов
                if str(product) not in existing_products:  # Проверка наличия продукта в списке
                    file.write(str(product) + '\n')  # Запись нового продукта в файл
                else:
                    print(f'Продукт {product.name} уже есть в магазине')  # Вывод сообщения о существующем продукте


# Пример использования
s1 = Shop()  # Создание объекта класса Shop
p1 = Product('Potato', 50.5, 'Vegetables')  # Создание объекта класса Product
p2 = Product('Spaghetti', 3.4, 'Groceries')  # Создание объекта класса Product
p3 = Product('Potato', 5.5, 'Vegetables')  # Создание объекта класса Product

print(p2)  # Вывод строки представления объекта

s1.add(p1, p2, p3)  # Добавление продуктов в магазин

print('Первый запуск:')
print(s1.get_products())  # Вывод списка продуктов

s1.add(p1, p2, p3)  # Попытка повторного добавления продуктов

print('Второй запуск:')
print(s1.get_products())  # Вывод обновленного списка продуктов