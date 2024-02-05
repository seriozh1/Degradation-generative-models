import random


def generate_operation():
    operations = ['+', '-', '*', '/']
    return random.choice(operations)


def generate_expression(min_n=-100, max_n=100):
    num1 = random.randint(min_n, max_n)
    num2 = random.randint(min_n, max_n)
    operation = generate_operation()
    if operation == '/' and num2 == 0:
        num2 = 1  # need to think if it's ok to substitute with 1
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
