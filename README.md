# Pensamiento Algoítmico
Isabella Agudelo y Camilo Alfonso Rodríguez


# CÁLCULO DE DAÑO POR ZONA EN APEX LEGENDS

# Introducción
Este proyecto tieme como objetivo documentar el entendimiento de los estudiantes en el uso de los programas vistos en clase tales como C++ y Python. Se proponé una situación con el propósito de que los estudiantes construyan un código utilizando herramientas como variables, condicionales, bucles y otros conceptos aprendidos en clase. El informe busca documentar los códigos, explicar su funcionamiento y los erroers posibles que se puedan dar al resolver el problema. 

# _INFORME_
# Problema
En Apex Legends, el daño de la zona es un mecanismo clave que obliga a los jugadores a moverse
hacia áreas seguras a medida que el círculo se cierra. El daño de la zona aumenta progresivamente
dependiendo del círculo en el que te encuentres. Tu tarea es calcular el daño total que recibirá un
jugador si permanece en la zona durante un tiempo determinado.
Dado el círculo actual y el tiempo t (en segundos) que un jugador pasa en la zona, debes calcular el
daño total recibido. El daño por segundo depende del círculo de la siguiente manera:

 1. Círculo 1: 2 de daño por segundo.
 2. Círculo 2: 5 de daño por segundo.
 3. Círculo 3: 10 de daño por segundo.
 4. Círculo 4 o mayor: 25 de daño por segundo.

# Requisitos Funcionales y No Funcionales
 # _Funcionales_
  1. Definir variables del círculo en el que se encuentra 
  2. Definir variables del tiempo que se quedó en el círculo
  3. Calcular el daño recibido dependiendo del circulo en el que se encuentre y el tiempo que duró en él
  4. Validar que el usuario haya ingresado números enteros mayores a 0 para el círculo
  5. Validar que el usuario haya ingresado números decimales mayores o iguales a 0
 # _No funcionales_
  1. No permitir la entrada de otros carácteres fuera de los anteriores mencionados
  2. Claro y consciso
  3. Utilizar correctamente los lenguajes de C++ y Python con lo que se ha enseñado en clase

# Casos de Uso Principales
Este programa puede ser utilizado como base para otros programas que necesiten de dos variables y calcular algún efecto recibido de acuerdo a los datos leídos
 1. Juegos con diferentes mecánicas que buscan calcular daño en base al tiempo o tiempo que permanezca en determinada zona
 2. Cálculo de exposición a sustancias peligrosas, un programa que dicte que tan dañino es estar en contacto con ciertos químicos por un determinado tiempo (sus variables podrían ser PH y tiempo)
 3. Consumo de energía, un programa que calcule el consumo de recursos y la contaminación que se está dando (sus variables podrían ser concentración de contaminantes y tiempo de su exposición)

# Identificación de entradas, procesos y salidas esperadas
 1. Entrada de datos:
   - número del círculo (c)
   - tiempo que pasó en el círculo (t)
 2. Procesamiento de datos:
   - Se define que si el cículo es 1 entonces se hará la operación t * 2
   -  Se define que si el cículo es 2 entonces se hará la operación t * 5
   - Se define que si el círculo es 3 entonces se hará la operación t * 10
   - Se define que si el círculo es 4 o más entonces se hará la operación t * 25
   - Se define que si el círculo es 0 entonces se escribirá "usted no ha recibido daño"
3. Salidas:
  - Se imprime un mensaje indicando cuál fue el daño recibido
  - Se imprime un mensaje indicando que no recibió daño

# Justificación de la solución    
Para resolver este problema, se le pide al ususario ingresar dos datos; el círculo en el que se encuentra y el tiempo que ha pasado en el círculo. Dependiendo de la situación del usuario se calculará la cantidad del daño recibido. Utilizamos el condicional if para cubrir cada uno de los casos posibles
# _Estrategia_
El programa sigue los siguientes pasos:
 1. le pide al usuario que ingrese el círculo en el que se encuentra
 2. le pide al usuario que ingrese el tiempo que se quedó en el círculo
 3. el programa hace una operación dependiendo del círculo que se encuentre por medio del condicional if
     - círculo 0: no recibe daño
     - círculo 1: t * 2
     - círculo 2: t * 5
     - círculo 3: t * 10
     - círculo 4 o más: t * 25
Concluimos que esta es la forma más efectiva de hacer el algorítmo puesto que cubre todas las posibilidades de daño que pueda recibir el usuario, así también evitando ampliar el código de manera innecesaria (por ejemplo hacer más bloques de la cuenta al no querer usar un condicional)

# _Soluciones alternativas_
Con lo que hemos visto en clase no podemos llegar aún a una solución alternativa

# Diagrama de Flujo




![sin_titulo](https://github.com/user-attachments/assets/c0411292-2e0f-408e-b9df-afaaa21d73a3)

# Código en Python
```python
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

```

# Código C++
```cpp
#include <iostream> //Biblioteca que permite la entrada y salida de datos

int c; //Variable que almacena el círculo en el que se encuentra
float t; //Variable que almacena el tiempo en segundos en el que estuvo en el círculo
int main (){
    //Se le pide al usuario que ingrese el numero del circulo en el que está 
    std::cout << "Escriba el círculo en el que se encuentra" << std::endl;
    std::cin >> c;
    //Se le pide al usuario que ingrese el tiempo en segundos en el que estuvo en el círculo
    std::cout << "Escriba el tiempo en segundos en el que estuvo en el círculo" << std::endl;
    std::cin >> t;
    //Se evalúa que el tiempo ingresado sea coherente
   if (t>=0){
       //Se evalua en que circulo está el usuario 
          if(c==1){
         float a = 2*t; //Si el circulo es 1, se multiplica el tiempo por 2
         std::cout << "Daño total recibido: " << a << std::endl; //Se imprime el daño total recibido
     } else {
         if(c==2){
             float b = 5*t; //Si el circulo es 2, se multiplica el tiempo por 5
             std::cout << "Daño total recibido: " << b << std::endl; //Se imprime el daño total recibido
         } else {
             if(c==3){
                 float d = 10*t;  //Si el circulo es 3, se multiplica el tiempo por 10
                 std::cout << "Daño total recibido: " << d << std::endl; //Se imprime el daño total recibido
             } else {
                 if(c>=4){
                     float e = 25*t;  //Si el circulo es 4 o mas, se multiplica el tiempo por 25
                     std::cout << "Daño total recibido: " << e << std::endl; //Se imprime el daño total recibido
                 } else{
                     if (c==0){
                         //Para casos en los que el circulo sea igual a 0
                         std::cout << "Usted no ha recibido daño";
                     } else
                         //Para casos en el que el círculo no tenga coherencia o no sea ingresado en el formato requerido
                     std::cout << "Por favor ingrese el círculo en el que se encuentra como un entero positivo";
                 }
             }
         }
     }
   }else{
       //Para casos en el que el tiempo no tenga coherencia o no sea ingresado en el formato requerido 
       std::cout << "Por favor ingrese el tiempo como un real positivo";
   }

return 0;
}
```


<h1>DOCUMENTACIÓN</h1>

# PYTHON

# Instalación y ejecución del programa (Windows)
1. Descarga python en su página oficial o en Microsoft Store, preferiblemente la versión más actual.
2. Descarga Visual Studio Code.
3. Ya con Visual Studio descargado, en el área de extensiones, se instalan las necesarias para python.
4. Crea una carpeta en tus archivos donde vayas a guardar tus códigos.
5. Abre VS Code, selecciona "Abrir carpeta" y elige la carpeta creada.
6. Crea un archivo "nombre.py" y asegúrate de que tenga la extensión ".py".
7. Escribe el código necesario.
8. Al momento de terminar, debes ir a la parte superior de la pantalla en el apartado de “Run” o “Ejecutar” en español, paso seguido, se elige la opción de “Start Debugging” o “Iniciar depurado”, o de manera más simplificada puedes usar el atajo de la tecla “F5” que inicia la ejecución del programa.
8. En la parte inferior de visual studio code se mostrará un apartado llamado “Terminal” en el cual se deben ingresar los datos solicitados para la ejecución del código. 

# Instalación y ejecución del programa (Linux)
1. Abre la terminal 
2. Verifica si python está instalado usando el comando
```
python3 –versión
```
4. Si no está instalado usa los comandos
 ```
sudo apt install python3 -y  # Debian/Ubuntu
 sudo dnf install python3      # Fedora
sudo pacman -S python         # Arch Linux
```
3. Crea una carpeta donde vayas a guardar tus proyectos y luego crea un archivo “nombre.py” y asegúrate de que tenga la extensión “.py” usando los siguientes comandos
```
mkdir ~/proyectos_python && cd ~/proyectos_python
nano nombre.py
```
5. Escribe el código necesario.
6. Ejecuta el programa con el comando
```
python3 nombre.py
```

# Instalación y ejecución del programa (MAC)
1. Abre la terminal 
2. Verifica si python está instalado usando el comando
```
python3 –versión
```
4. Si no está instalado usa el comando
```	
brew install python
```
3. Crea una carpeta donde vayas a guardar tus proyectos y luego crea un archivo “nombre.py” y asegúrate de que tenga la extensión “.py” usando los siguientes comando
```
mkdir ~/proyectos_python && cd ~/proyectos_python
nano nombre.py
```
4. Escribe el código necesario.
5. Ejecuta el programa con el comando
```
python3 nombre.py
```

# C++

# Instalación y ejecución del programa (Windows)
1. Descarga un compilador de C++ como podría ser “MinGW”
2. Durante la instalación selecciona los componentes de "mingw32-gcc-g++".
2. Asegúrate de que configurar el compilador a tu gusto, diferentes estilos, idioma, tipografía, etc.
3. Configura la variable de entorno, ve a "Panel de Control" > "Sistema" > "Configuración avanzada del sistema".
4. En "Variables de entorno", edita la variable "Path" y agrega la ruta de MinGW (ejemplo: C:\MinGW\bin).
5. Descarga Visual Studio Code.
6. Ya con Visual Studio descargado, en el área de extensiones, se instalan las necesarias para C++.
7.  Crea una carpeta en tus archivos donde vayas a guardar tus códigos.
8. Abre VS Code, selecciona "Abrir carpeta" y elige la carpeta creada.
9.  Crea un archivo "nombre.c++" y asegúrate de que tenga la extensión ".c++", también es válido usar “.cc” o “.cpp”.
10. Escribe el código necesario
11. Al momento de terminar el código, para ejecutarlo abre la terminal, en la parte superior de la pantalla ve al menú “View” o “ver” y luego selecciona “Terminal” o puedes usar el atajo “ctrl-ñ” en español o “ctrl-\” en ingles con lo que se abrirá directamente el apartado de terminal.
12. En la terminal ejecuta el comando “g++ nombre.c++ -o programa.exe”.
13. Si no aparece ningún error, se creará un archivo ejecutable llamado “programa.exe” en la carpeta creada anteriormente.
14. En la terminal ejecuta el comando “.\programa.exe”, si el programa fue compilado de manera correcta, se mostrará la ejecución del código ingresado anteriormente.

# Instalación y ejecución del programa (Linux)
1.  Abre la terminal
2.  Instala el compilador de C++ usando los comandos
```
sudo apt install g++ -y  # Debian/Ubuntu
sudo dnf install gcc-c++  # Fedora
sudo pacman -S gcc        # Arch Linux
```
3. Crea una carpeta donde vayas a guardar tus proyectos y luego crea un archivo “nombre.cpp” y asegúrate de que tenga la extensión “.cpp” usando el siguiente comando
```
mkdir ~/proyectos_cpp && cd ~/proyectos_cpp
nano nombre.cpp
```
4. Escribe el código necesario 
5. compila y ejecuta el programa con los siguientes comandos
```
g++ nombre.cpp -o nombre
./nombre
```

# Instalación y ejecución del programa (MAC)
1. Abre la terminal.
2. Instala el compilador de C++ usando el comando.
```
xcode-select –install
```
3. Crea una carpeta donde vayas a guardar tus proyectos y luego crea un archivo “nombre.cpp” y asegúrate de que tenga la extensión “.cpp” usando el siguiente comando
```
mkdir ~/proyectos_cpp && cd ~/proyectos_cpp
nano nombre.cpp
```
4. Compila y ejecuta el programa con los siguientes comandos
```
g++ nombre.cpp -o nombre
./nombre
```

# Guía de uso
 1. Al momento de que se ejecute el codigo se le pedirá al usuario que ingrese el numero del círculo en el que se encuentra (solo se aceptarán números enteros mayores a 0)
 2. Luego se le pedirá al usuario el tiempo que pasó en el círculo.
 3. Se ejecutara el programa y mostrara el daño recibido dependiendo del circulo y el tiempo que se haya pasado en este.

# Documentacion tecnica
En el codigo podemos evidenciar comentarios que explican el funcionamiento de cada parte del codigo. 

# Ejemplo de codigo
- Escriba el circulo en el que se encuentra: 3 <--(Digita el numero del circulo en el que te encuentras)
- Escriba el tiempo en segundos el que estuvo en el círculo: 45 <--(Digita el tiempo en segundo que estuviste en el circulo)
- Daño total recibido: 450.0 <--(El programa muestra el calculo de el daño que hace el circulo ingresado por el tiempo en segundos que estuviste en este)

# Errores comunes
 1. Ingreso de valores negativos:
    - problema: Si el usuario ingresa un número negativo en el tiempo o círculo, el programa no calcula el daño correctamente.
    - solucion: El programa envia un mensaje en el que aclara que no se permiten usar valores negativos.
    
 2. Ingreso de valores no numéricos:
    - problema: Si el usuario ingresa un valor que no sea un numero el programa fallara.
    - solucion: El codigo maneja una excepcion para que cuando se usen letras en lugar de numeros el programa envie un mensaje aclarando que no es un valor valido.

# Contribuciones
Este programa al ser de codigo abierto permite que cualquier persona pueda contribuir a este proyecto. 
