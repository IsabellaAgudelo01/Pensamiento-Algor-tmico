c= int(input("Escriba el círculo en el que se encuentra: "))
t=float(input("Escriba el tiempo en el que estuvo en el círculo: "))
#Revisamos que el valor del tiempo sea coherente
if t >= 0:
    if c == 1:
        print(f"Daño total recibido: {2 * t}")
    elif c == 2:
        print(f"Daño total recibido: {5 * t}")
    elif c == 3:
        print(f"Daño total recibido: {10 * t}")
    elif c >= 4:
        print(f"Daño total recibido: {25 * t}")
    elif c == 0:
        #Caso en el que círculo sea 0
        print("Usted no ha recibido daño")
    else:
        #En casos donde el círculo no esté en el formato requerido
        print("Por favor ingrese el círculo en el que se encuentra como un entero positivo")
else:
    #En casos donde el tiempo no esté en el formato requerido
    print("Por favor ingrese el tiempo como un real positivo")
