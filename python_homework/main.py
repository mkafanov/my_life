from statistics import mean

def total_revenue(purchases: list[dict]) -> float:
    revenue = sum([purchase['price'] * purchase['quantity'] for purchase in purchases])
    return revenue


def items_by_category(purchases: list[dict]) -> dict:
    categories = {}
    for purchase in purchases:
        if purchase['category'] in categories and purchase['item'] not in categories[purchase['category']]:
            categories[purchase['category']].append(purchase['item'])
        else:
            categories[purchase['category']] = [purchase['item']]
    return categories


def expensive_purchases(purchases: list[dict], min_price: float) -> list:
    return list(filter(lambda x: x['price'] >= min_price, purchases))


def average_price_by_category(purchases: list[dict]) -> dict:
    categories = {}
    for purchase in purchases:
        if purchase['category'] in categories:
            categories[purchase['category']].append(purchase['price'])
        else:
            categories[purchase['category']] = [purchase['price']]
    return {categorie: mean(price) for categorie, price in categories.items()}


def most_frequent_category(purchases: list[dict]) -> str:
    categories = {}
    for purchase in purchases:
        if purchase['category'] in categories:
            categories[purchase['category']] += purchase['quantity']
        else:
            categories[purchase['category']] = purchase['quantity']
    return max(categories.items(), key=lambda x: x[1])[0]


def form_report(purchases: list[dict]) -> None:
    revenue = total_revenue(purchases)
    items = items_by_category(purchases)
    over_one = expensive_purchases(purchases, 1.0)
    avg_price = average_price_by_category(purchases)
    mf_category = most_frequent_category(purchases)

    print(f'Общая выручка: {revenue}')
    print(f'Товары по категориям: {items}')
    print(f'Покупки дороже 1.0: {over_one}')
    print(f'Средняя цена по категориям: {avg_price}')
    print(f'Категория с наибольшим количеством проданных товаров: {mf_category}')


purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


form_report(purchases)