class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if self.isOperator(token):
                operand2 = stack.pop()
                operand1 = stack.pop()

                result = self.evaluate(token, operand1, operand2)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]


    def isOperator(self, token):
        return token == "+" or token == "-" or token == "*" or token == "/"


    def evaluate(self, token, operand1, operand2):
        if token == "+":
            return operand1 + operand2
        elif token == "-":
            return operand1 - operand2
        elif token == "*":
            return operand1 * operand2
        elif token == "/":
            return int(operand1 / operand2)
        else:
            return 0

        
