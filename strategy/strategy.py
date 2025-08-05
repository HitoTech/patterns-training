from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass


class NoDiscountStrategy(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price

class PercentageDiscountStrategy(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return (price * 75) / 100

class FixedDiscountStrategy(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price - 10