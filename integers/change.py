coins = [200, 100, 50, 20, 10, 5, 2, 1]


def change_greedy(amount):
    result = 0
    i = 0
    while amount > 0:
        result += int(amount / coins[i])
        amount %= coins[i]
        i += 1

    return result


def change_dynamic(amount):
    partial_results = []
    used_coins = []
    infinity = 10000000

    for i in range(0, amount + 1):
        partial_results.append(infinity)
        used_coins.append(infinity)

    partial_results[0] = 0

    number_of_coins = int(input('Enter number of coins'))

    for j in range(0, number_of_coins):
        coin_value = int(input('Enter next coin value'))
        for i in range(0, amount - coin_value + 1):
            if partial_results[i] + 1 < partial_results[i + coin_value]:
                partial_results[i + coin_value] = partial_results[i] + 1
                used_coins[i + coin_value] = coin_value

    if partial_results[amount] == infinity:
        print('Cannot give out specified value using given coins')
        return

    print(f'Amount {amount} can be given out using {partial_results[amount]} coins')
    print('Used coins:')
    i = amount
    while i > 0:
        print(used_coins[i])
        i -= used_coins[i]


amount = int(input('Enter amount'))
print('Greedy algorithm')
print(f'Amount {amount} can be given out using {change_greedy(amount)} coins')
print('Dynamic algorithm')
change_dynamic(amount)
