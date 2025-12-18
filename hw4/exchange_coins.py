def exchange(n):
    coins = [4, 8, 9]
    dp = [None] * (n + 1)  # for implementation this program we use dynamik programming
    last_sum = [-1] * (n + 1)
    last_coin = [-1] * (n + 1)
    dp[0] = 0  # start point for program
    for i in range(1, n + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] is not None:  # noqa: SIM102
                if dp[i] is None or dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    last_sum[i] = i - coin
                    last_coin[i] = coin
    if dp[n] is None:
        return None
    else:  # noqa: RET505
        change = []
        current_sum = n
        while current_sum > 0:
            coin = last_coin[current_sum]
            change.append(coin)
            current_sum = last_sum[current_sum]
        return change


try:  # use "try except". eg for non-numeric inputs
    num = int(input("Введите число для размена: "))
    if num < 0:
        print("-42!")
    else:
        result = exchange(num)
        if result:
            print(f"Размен числа {num}: {result}")
        else:
            print("-42!")


except:  # noqa: E722
    print("-42!")
