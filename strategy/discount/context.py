from strategy import DiscountStrategy


class PriceCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def get_final_price(self, price: float) -> float:
        return self.strategy.calculate(price)
