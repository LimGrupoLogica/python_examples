gato = 'robber'
animal = str("perro")
edad = 2
porcentaje = 10.5
esmacho = False
numero_grande = 35e3
print(numero_grande)
raton, perro, gallo = "robber", "robber", "robber"

textoLarog = """
    ksdjknsjdncjsnd
    skdncks



    cmsdmcnsdnjs
"""
print(textoLarog)
print(gato.upper())

print(raton)
print(perro)
print(gallo)

print(gato)
print(type(gato))
print(type(porcentaje))
print(type(esmacho))
if gato == 'kitty'and edad>=1 and edad <=5 and esmacho == False:
    print('soy kitty macho')
elif gato == 'robber'and(edad== 1 or edad== 2 or edad == 3)and esmacho == False:
    print('soy un gato del otro equipo')
else:
    print('soy un gato normal')



print(2)
print(3)
print(4)



edad = 50
esMayorDeEdaad = True
esHombre = True

if esMayorDeEdaad == True:
    if edad > 40:
        if esHombre == True:
            print("es adulto varon")

match edad:
    case 30 if esHombre == True:
        print("es un adulto joven varon")
    case 40 | 50 if esHombre == True:
        print("es un adulto mayor varon")
    case _:
        print("no se sabe la edad y posiblemente sea mujer")
