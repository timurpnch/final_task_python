import csv

import matplotlib.pyplot as plt


def read_sales_data(file_path: str) -> list:
    '''
    Функуия принимает на вход путь к файлу и возвращает список продаж.
    Продажи в свою очередь являются словарями
    :param file_path:str - путь до csv файла с разделителем ','
    :return sales_list:list - список со словарями, которые имеют ключи
                              product_name, quantity, price, date.
    '''

    sales_list = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            sales_dict = {'product_name': row[0],
                          'quantity': int(row[1]),
                          'price': float(row[2]),
                          'date': row[3]}
            sales_list.append(sales_dict)

    return sales_list


def total_sales_per_product(sales_data: list) -> dict:
    '''
    Функция, которая принимает список продаж и возвращает словарь,
    где ключ - название продукта, а значение - общая сумма
    :param sales_data:list - список продаж, сформированный функцией read_sales_data
    :return total_sales_dict:dict - словарь с парами (товар:общая сумма)
    '''

    total_sales_dict = {}

    for sale in sales_data:
        if sale['product_name'] in total_sales_dict.keys():
            total_sales_dict[sale['product_name']] += sale['quantity'] * sale['price']
        else:
            total_sales_dict[sale['product_name']] = sale['quantity'] * sale['price']

    return total_sales_dict


def sales_over_time(sales_data: list) -> dict:
    '''
    Функция, которая принимает список продаж и возвращает словарь,
    где ключ - дата, а значение общая сумма продаж за эту дату
    :param sales_data:list - список продаж, сформированный функцией read_sales_data
    :return date_sales_dict - словарь с парами (дата:общая сумма)
    '''

    date_sales_dict = dict()

    for sale in sales_data:
        if sale['date'] in date_sales_dict.keys():
            date_sales_dict[sale['date']] += sale['quantity'] * sale['price']
        else:
            date_sales_dict[sale['date']] = sale['quantity'] * sale['price']

    return date_sales_dict


def main():
    data_sales = read_sales_data('sales.csv')
    sales_per_product = total_sales_per_product(data_sales)
    sales_over_date = sales_over_time(data_sales)

    max_profit_products = [key for key, value in sales_per_product.items() if value == max(sales_per_product.values())]
    max_profit_dates = [key for key, value in sales_over_date.items() if value == max(sales_over_date.values())]

    print(f"Продукты, которые принесли наибольшую выручку: {', '.join(max_profit_products)}")
    print(f"Дни с наибольшой суммой продаж: {', '.join(max_profit_dates)}")

    plt.xlabel('Товары')  # Подпись для оси х
    plt.ylabel('Общая сумма продаж')  # Подпись для оси y
    plt.title('График общей суммы продаж по каждому продукту')
    plt.plot(sales_per_product.keys(), sales_per_product.values(), color='green', marker='o', markersize=7)
    plt.show()

    plt.xlabel('Даты')
    plt.ylabel('Общая сумма продаж')
    plt.title('График общей суммы продаж по дням')
    plt.plot(sales_over_date.keys(), sales_over_date.values(), color='red', marker='o', markersize=7)
    plt.show()


if __name__ == '__main__':
    main()
