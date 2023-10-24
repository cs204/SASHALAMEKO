amount_due=50
while amount_due > 0:
    print(f"Нужная сумма: {amount_due}")
    coin = int(input("Вставьте монету: "))
    if coin in [50, 20, 10, 5]:
        amount_due=amount_due-coin
print(f"Ваша сдача: {abs(amount_due)}")
