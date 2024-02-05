import random


def generate_operation():
    operations = ['+', '-', '*', '/']
    return random.choice(operations)


def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = generate_operation()
    if operation == '/' and num2 == 0:
        num2 = 1  # need to think if it's to substitute with 1
    return num1, operation, num2


def calculate_result(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = round(num1 / num2)
    return result


def generate_text():
    num1, operation, num2 = generate_expression()
    result = calculate_result(num1, operation, num2)
    text = f"{num1} {operation} {num2} = {result}"
    return text


if __name__ == "__main__":
    number_samples = 10**5
    samples = [generate_text() for _ in range(number_samples)]

    with open("arithmetic_samples.txt", "w") as file:
        for sample in samples:
            file.write(sample + "\n")
