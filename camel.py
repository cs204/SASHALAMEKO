txt=input("Верблюжий стиль: ")
con=[]
for s in txt:
    if s in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        con.append("_")
        con.append(s.lower())
    else:
        con.append(s)
txt="".join(con)

print(txt)