coins={10:0,5:0,2:0,1:0}
amount=int(input("Enter the amount: "))
for coin in coins.keys():
    if amount>0:
        coins[coin]=amount//coin
        amount-=coins[coin]*coin
    else:
        break

print("The number of coins are:")
for coin in coins:
    print(f"{coins[coin]} coins of Rs.{coin}")