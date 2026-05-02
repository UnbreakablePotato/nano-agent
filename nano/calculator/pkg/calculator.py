import math

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.unary_operators = {
            "sin": math.sin,
            "cos": math.cos,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "sin": 3,  # Higher precedence than binary ops
            "cos": 3,
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        # Tokenize assuming space separation, might need more advanced tokenization for complex cases
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        values = []  # Stack for numbers
        operators = []  # Stack for operators

        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token in self.operators:
                # Handle binary operators
                while (
                    operators
                    and operators[-1] in self.precedence # Ensure operator is in precedence map
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            elif token in self.unary_operators:
                # Handle unary operators - simply push them onto the operator stack
                operators.append(token)
            else:
                # Handle numbers
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")
            i += 1

        # Apply any remaining operators in the stack
        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()

        if operator in self.unary_operators:
            if not values:
                raise ValueError(f"not enough operands for unary operator {operator}")
            operand = values.pop()
            values.append(self.unary_operators[operator](operand))
        elif operator in self.operators:
            if len(values) < 2:
                raise ValueError(f"not enough operands for binary operator {operator}")
            b = values.pop()
            a = values.pop()
            values.append(self.operators[operator](a, b))
        else:
            raise ValueError(f"unknown operator: {operator}")

if __name__ == "__main__":
    calculator = Calculator()
    print("Calculator started. Type 'exit' to quit.")
    while True:
        expression = input("Enter expression: ")
        if expression.lower() == 'exit':
            break
        try:
            result = calculator.evaluate(expression)
            if result is not None:
                print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
