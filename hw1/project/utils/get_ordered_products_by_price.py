def get_ordered_products_by_price(products: list) -> list:
    return sorted(products, key= lambda product: product.price, reverse=True)
