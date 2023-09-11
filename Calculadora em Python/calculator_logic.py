class Calculator:
    def __init__(self):
        self.result = None
        self.display = []
        self.operation = ['+', '-', '*', '/']

    def sum(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def times(self, x, y):
        return x * y

    def division(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        else:
           return int(x / y)

    def update(self, user_input):
        if user_input == "C" or (self.display and self.display[0] == "Error: Division by zero"):
            self.display.clear()

        try:
            value = int(user_input)
            if self.display and isinstance(self.display[-1], int):
                self.display[-1] = int(str(self.display[-1]) + str(user_input))
            else:
                self.display.append(value)
        except ValueError:
            if user_input in ['+', '-', '*', '/']:
                if self.display[-1] in ['+', '-', '*', '/']:
                    self.display[-1] = user_input
                else:
                    self.display.append(user_input)
            else:
                print("Error: Invalid input, please enter a number or an operator")

    def perform_calculator(self):
        if not self.display:
            return "Display is empty"

        result = self.display[0]
        operator = None

        for token in self.display[1:]:
            if isinstance(token, str):
                operator = token
            else:
                if operator == '+':
                    result = self.sum(result, token)
                elif operator == '-':
                    result = self.subtraction(result, token)
                elif operator == '*':
                    result = self.times(result, token)
                elif operator == '/':
                    result = self.division(result, token)

        self.result = result
        self.display.clear()
        self.display.append(result)
        return self.result
