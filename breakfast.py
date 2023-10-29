menu = {
"кофе": 20.00,
"чай": 10.00,
"булочка": 5.00,
"салат": 30.40,
"пирожное": 45.50
}
sum = 0
try:
    while True:
        bl = input("Блюдо: ")
        if bl in menu:
            sum += menu[bl]
except EOFError:
    print(f"\nСумма: {sum:.2f}")