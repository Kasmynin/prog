class JacketFabric:
    def calculate_fabric_consumption(self, size):
        fabric_requirements = {"S": 1.5, "M": 1.8, "L": 2.1, "XL": 2.4}
        return fabric_requirements.get(size)

class TrousersFabric:
    def calculate_fabric_consumption(self, size):
        fabric_requirements = {"S": 1.0, "M": 1.2, "L": 1.4, "XL": 1.6}
        return fabric_requirements.get(size)

class SuitFabric:
    def calculate_fabric_consumption(self, size):
        fabric_requirements = {"S": 3.5, "M": 4.0, "L": 4.5, "XL": 5.0}
        return fabric_requirements.get(size)