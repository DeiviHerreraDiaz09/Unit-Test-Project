def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total


def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0


def test_calculate_total_with_single_product():
    products = [{"name": "Notebook", "price": 5}]
    assert calculate_total(products) == 5


def test_calculate_total_with_single_products():
    print("Entró a la función")
    products = [
        {"name": "Notebook", "price": 5},
        {"name": "Book", "price": 3},
        {"name": "Pencil", "price": 5},
    ]
    assert calculate_total(products) == 13


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_single_products()
