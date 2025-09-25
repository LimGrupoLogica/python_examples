n = int(input("ingrese altura del arbol: "))
sep=n

for i in range(n + 1):
    print(" " * sep ,"* " * i)
    sep -= 1