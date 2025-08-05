from context import PriceCalculator
from strategy import FixedDiscountStrategy, NoDiscountStrategy, PercentageDiscountStrategy

calculator = PriceCalculator(PercentageDiscountStrategy())
final = calculator.get_final_price(200)
print(final)

calculator = PriceCalculator(NoDiscountStrategy())
final = calculator.get_final_price(200)
print(final)

calculator = PriceCalculator(FixedDiscountStrategy())
final = calculator.get_final_price(200)
print(final)