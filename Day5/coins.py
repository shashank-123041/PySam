coins = {10: 0, 5: 0, 2: 0, 1: 0}
amount = int(input())
for coin in coins: coins[coin], amount = amount // coin, amount % coin
print(*[f"{v} coins of Rs.{k}" for k, v in coins.items() if v], sep="\n")
