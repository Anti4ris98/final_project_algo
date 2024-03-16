import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Словник для зберігання кількості випадінь кожної суми
    sum_counts = {sum_: 0 for sum_ in range(2, 13)}
    
    # Симуляція кидків
    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        sum_counts[roll_sum] += 1
    
    # Обчислення ймовірностей
    probabilities = {sum_: count / num_rolls for sum_, count in sum_counts.items()}
    
    return probabilities

def plot_probabilities(probabilities):
    # Створення списків для значень і їх ймовірностей
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')
 # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()

# Кількість кидків
num_rolls = 10000

# Симуляція кидків і обчислення ймовірностей
probabilities = simulate_dice_rolls(num_rolls)

# Відображення ймовірностей на графіку
plot_probabilities(probabilities)
