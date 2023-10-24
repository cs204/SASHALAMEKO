def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v: str):
    v=float(v.replace("ft", ""))
    v=v*0.3048
    return v

main()