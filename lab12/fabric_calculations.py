def calculate_fabric_consumption(item, size):
    """Рассчитывает расход ткани в зависимости от размера"""
    fabric_requirements = {
        "Пиджак": {"S": 1.5, "M": 1.8, "L": 2.1, "XL": 2.4},
        "Брюки": {"S": 1.0, "M": 1.2, "L": 1.4, "XL": 1.6},
        "Костюм-тройка": {"S": 3.5, "M": 4.0, "L": 4.5, "XL": 5.0}
    }
    if item in fabric_requirements and size in fabric_requirements[item]:
        return fabric_requirements[item][size]
    else:
        return None