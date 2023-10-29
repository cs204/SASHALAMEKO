dr=input("Дробь: ")
x, y= dr.split("/")
x=int(x)
y=int(y)
dr=int(x/y*100)
try:
    if dr<=1:
        print("E")
    elif dr>=99:
        print("F")
    else:
        print(f"{dr}%")
except (ValueError, ZeroDivisionError):
    pass
