import os
from create_dataset import calculate_result


def calculate_accuracy(filename):
    total_count = 0
    skiped_count = 0
    correct_count = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split()
            if len(parts) < 5 or line.endswith('-'):
                skiped_count += 1
                continue
            num1 = int(parts[0])
            operation = parts[1]
            num2 = int(parts[2])
            result = float(parts[4])
            if calculate_result(num1, operation, num2) == result:
                correct_count += 1
            else:
                print("Incorrect result: ", line)
            total_count += 1
    accuracy = (correct_count / total_count) * 100
    return accuracy, total_count, skiped_count


if __name__ == "__main__":
    filename = os.path.join(
        os.path.dirname(__file__),
        'generated_samples.txt'
    )

    accuracy, total_count, skiped_count = calculate_accuracy(filename)
    print("total_count:", total_count)
    print("skiped_count:", skiped_count)
    print("accuracy:", accuracy)
