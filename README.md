# Pensamiento Algoítmico
Isabella Agudelo y Camilo Alfonso Rodríguez


# CÁLCULO DE DAÑO POR ZONA EN APEX LEGENDS

# Introducción
Este proyecto tiene como objetivo documentar el entendimiento de los estudiantes en el uso de los distintos lenguajes de programación vistos en clase tales como C++ y Python y el uso de distintas herramientas como ambientes o compiladores necesarios para la ejecución de un código en los distintos sistemas operativos. Se propone una situación con el propósito de que los estudiantes construyan un código utilizando variables, condicionales, bucles y otros conceptos aprendidos en clase para hallar la solución al problema especificado. El informe busca documentar los códigos, explicar su funcionamiento y los errores posibles que se puedan dar al resolver el problema.  

# <h1>INFORME</h1> 

<h2>Problema</h2>
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


 <h2>Requisitos Funcionales y No Funcionales </h2>
 # <h3>Funcionales</h3>
  1. Definir variables del círculo en el que se encuentra 
  2. Definir variables del tiempo que se quedó en el círculo
  3. Calcular el daño recibido dependiendo del circulo en el que se encuentre y el tiempo que duró en él
  4. Validar que el usuario haya ingresado números enteros mayores a 0 para el círculo
  5. Validar que el usuario haya ingresado números decimales mayores o iguales a 0
     
# <h3>No Funcionales</h3>
  1. No permitir la entrada de otros carácteres fuera de los anteriores mencionados
  2. Claro y consciso
  3. Utilizar correctamente los lenguajes de C++ y Python con lo que se ha enseñado en clase

# <h2>Casos de Uso Principales</h2>
Este programa puede ser utilizado como base para otros programas que necesiten de dos variables y calcular algún efecto recibido de acuerdo a los datos leídos
 1. Juegos con diferentes mecánicas que buscan calcular daño en base al tiempo o tiempo que permanezca en determinada zona
 2. Cálculo de exposición a sustancias peligrosas, un programa que dicte que tan dañino es estar en contacto con ciertos químicos por un determinado tiempo (sus variables podrían ser PH y tiempo)
 3. Consumo de energía, un programa que calcule el consumo de recursos y la contaminación que se está dando (sus variables podrían ser concentración de contaminantes y tiempo de su exposición)

# <h2>Identificación de entradas, procesos y salidas esperadas</h2>
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

# <h2>Justificación de la solución</h2>    
Para resolver este problema, se le pide al ususario ingresar dos datos; el círculo en el que se encuentra y el tiempo que ha pasado en el círculo. Dependiendo de la situación del usuario se calculará la cantidad del daño recibido. Utilizamos el condicional if para cubrir cada uno de los casos posibles
# <h2>_Estrategia_</h2>
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

# <h2>_Soluciones alternativas_</h2>
Con lo que hemos visto en clase no podemos llegar aún a una solución alternativa



















<h1>DOCUMENTACIÓN</h1>

# Python
# Instalación y ejecución del programa (Windows)
1. Descarga python en su página oficial o en Microsoft Store, preferiblemente la versión más actual.
2. Descarga Visual Studio Code.
3. Ya con Visual Studio descargado, en el área de extensiones, se instalan las necesarias para python.
4. Crea una carpeta en tus archivos donde vayas a guardar tus códigos.
5. Abre VS Code, selecciona "Abrir carpeta" y elige la carpeta creada.
6. Crea un archivo "nombre.py" y asegúrate de tener la extensión ".py".
7. Escribe el código necesario.
8. Al momento de terminar, debes ir a la parte superior de la pantalla en el apartado de “Run” o “Ejecutar” en español, paso seguido, se elige la opción de “Start Debugging” o “Iniciar depurado”, o de manera más simplificada puedes usar el atajo de la tecla “F5” que inicia la ejecución del programa.
8. En la parte inferior de visual studio code se mostrará un apartado llamado “Terminal” en el cual se deben ingresar los datos solicitados para la ejecución del código. 

# Instalación C++
Para ejecutar el programa en C++ se siguen los siguientes pasos:
 1. Descarga un compilador de C++
 2. Asegúrate de que configurar el compilador a tu gusto, diferentes estílos, idioma, tipografía, etc
 3. Descarga Visual Studio Code
 4. Ya con Visual Studio descargado se instala la extensión de C++
 5.  Crea una carpeta en tus archivos donde vayas a guardar tus códigos
 6.  Abre la cartpeta y crea un archivo "Nombre.c++", asegúrate de tener el ".c++"

# Guía de uso
 1. Abrir Visual Studio Code y crear dos archivos, cada uno con su respectiva terminación (".py" y ".c++")
 2. Ejecutamos el código
 3. Se le pedirá al usuario el círculo en el que se encuentra (solo se aceptarán números enteros mayores a 0)
 4. Se le pedirá al usuario el tiempo que pasó en el círculo (solo se aceptarán floats)
