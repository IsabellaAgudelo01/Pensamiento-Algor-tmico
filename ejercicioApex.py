try: #Se usa para manejar excepciones, en este caso la de si se ingresan valores que no sean numeros
#Se le pide al usuario que ingrese el numero del circulo en el que está
    c= int(input("Escriba el círculo en el que se encuentra: "))
#Se le pide al usuario que ingrese el tiempo en el que estuvo en el círculo
    t=float(input("Escriba el tiempo en segundos en el que estuvo en el círculo: "))
#Se verifica el tipo de valor que se ingreso para el tiempo
    if t >= 0:
    #Se evalua en que circulo está el usuario y se calcula el daño recibido
        if c == 1:
            print(f"Daño total recibido: {2 * t}") #Si el circulo es 1, se multiplica el tiempo por 2 y se imprime el valor recibido 
        elif c == 2:
            print(f"Daño total recibido: {5 * t}") #Si el circulo es 2, se multiplica el tiempo por 5 y se imprime el valor recibido 
        elif c == 3:
            print(f"Daño total recibido: {10 * t}") #Si el circulo es 3, se multiplica el tiempo por 10 y se imrprime el valor recibido 
        elif c >= 4:
            print(f"Daño total recibido: {25 * t}") #Si el circulo es 4 o mas, se multiplica el tiempo por 25 y se imprime el valor recibido
        elif c == 0:
            print("Usted no ha recibido daño") #Para casos en los que el circulo sea igual a 0
        else:
            print("Por favor ingrese el círculo en el que se encuentra como un entero positivo") #Para casos en el que el círculo no sea coherente o no esté en el formato requerido
    else:
        print("Por favor ingrese el tiempo como un real positivo") #Para casos en el que el tiempo no sea coherente o no esté en el formate requerido 
except ValueError:
    print("Por favor ingrese valores numéricos válidos") #Para casos en los que el valor ingresado no sea un número
