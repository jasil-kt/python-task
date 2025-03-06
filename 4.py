
arr = [44,30,24,32,35,30,40,38,15]
def ArrayChallenge(arr):
    min_price = arr[0]
    max_profit = 0

    for price in arr[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit

print(ArrayChallenge(arr))
