
n=int(input("ingrese limite: "))
acc = 1
out = ""

for i in range(n):
    out = str(acc) + " " + out
    print(out)
    acc += 2
