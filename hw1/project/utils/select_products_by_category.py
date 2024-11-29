def select_products_by_category(products: list, category: str) -> list:
    return list(filter(lambda product: product.category == category, products))
