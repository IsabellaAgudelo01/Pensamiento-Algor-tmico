#Se le pide al usuario que ingrese el numero del circulo en el que está
c = int(input("Escriba el círculo en el que se encuentra: "))
#Se le pide al usuario que ingrese el tiempo en el que estuvo en el círculo
t = float(input("Escriba el tiempo en el que estuvo en el círculo: "))

#Se evalua en que circulo está el usuario y se calcula el daño recibido
if c == 1: 
    a = 2*t #Si el circulo es 1, se multiplica el tiempo por 2
    print (f"Daño total recibido: {a}") #Se imprime el daño total recibido
elif c == 2:
    b = 5*t #Si el circulo es 2, se multiplica el tiempo por 5
    print (f"Daño total recibido: {b}") #Se imprime el daño total recibido
elif c == 3:
    d = 10*t #Si el circulo es 3, se multiplica el tiempo por 10
    print (f"Daño total recibido: {d}") #Se imprime el daño total recibido
elif c >= 4:
    e = 25*t #Si el circulo es 4 o mas, se multiplica el tiempo por 25
    print(f"Daño total recibido: {e}") #Se imprime el daño total recibido
else: 
    #Para casos en los que el circulo sea menor a 1
    print("Usted no ha recibido daño") 