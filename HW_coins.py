#Жадібний алгоритм
def find_coins_greedy(amount, coins):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

#Динамічний алгоритм
def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)  # мінімальна кілкість монет
    dp[0] = 0  # остання монета для цієї суми

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    result = {}
    while amount > 0:
        for coin in coins:
            if amount - coin >= 0 and dp[amount - coin] == dp[amount] - 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break
    return result


coins = [50, 25, 10, 5, 2, 1]

greedy_result = find_coins_greedy(123, coins)
dp_result = find_min_coins(123, coins)


print(f"Жадібний алгоритм: {greedy_result}\nДинамічний алгоритм: {dp_result}")

