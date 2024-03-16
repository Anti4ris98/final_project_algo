def greedy_algorithm(items, budget):
    # Сортування елементів за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    chosen_items = []

    for item, info in sorted_items:
        if budget >= info["cost"]:
            budget -= info["cost"]
            total_calories += info["calories"]
            chosen_items.append(item)

    return chosen_items, total_calories

def dynamic_programming(items, budget):
    # Перетворення словника у список для легшого доступу
    items_list = [(name, info["cost"], info["calories"]) for name, info in items.items()]
    n = len(items_list)
    # Ініціалізація таблиці DP
    dp = [[0 for x in range(budget + 1)] for y in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if items_list[i-1][1] <= w:
                dp[i][w] = max(items_list[i-1][2] + dp[i-1][w-items_list[i-1][1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Відновлення набору страв
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(items_list[i-1][0])
            w -= items_list[i-1][1]

    chosen_items.reverse()
    total_calories = dp[n][budget]

    return chosen_items, total_calories

if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = 100 # Бюджет від якого віштовхуємось

    chosen_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:")
    print("Обрані варінти:", chosen_items_greedy)
    print("Сумма колорій:", total_calories_greedy)

    chosen_items_dp, total_calories_dp = dynamic_programming(items, budget)
    print("\nДинамічне програмування:")
    print("Обрані варінти:", chosen_items_dp)
    print("Сумма колорій:", total_calories_dp)