from nano.calculator.pkg.calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 7 * 2")
assert result == 17
print("Test passed!")