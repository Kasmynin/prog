from abc import ABC, abstractmethod

class ClothingItem(ABC):
    """Абстрактный базовый класс для предметов одежды."""

    @abstractmethod
    def calculate_fabric_consumption(self, size):
        """Абстрактный метод для расчета расхода ткани."""
        pass

    @abstractmethod
    def calculate_cost(self, fabric_price, accessories_cost):
        """Абстрактный метод для расчета стоимости."""
        pass

    @abstractmethod
    def __str__(self):
        """Абстрактный метод для строкового представления объекта."""
        pass