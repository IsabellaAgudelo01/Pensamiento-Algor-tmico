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
    número del círculo (c)
    tiempo que pasó en el círculo (t)
 2. Procesamiento de datos:
    Se define que si el cículo es 1 entonces se hará la operación t * 2
    Se define que si el cículo es 2 entonces se hará la operación t * 5
     Se define que si el círculo es 3 entonces se hará la operación t * 10
    Se define que si el círculo es 4 o más entonces se hará la operación t * 25
     Se define que si el círculo es 0 entonces se escribirá "usted no ha recibido daño"
3. Salidas:
   Se imprime un mensaje indicando cuál fue el daño recibido
   Se imprime un mensaje indicando que no recibió daño

# Justificación de la solución    






















# _DOCUMENTACIÓN_
# Instalación Python 
Para ejecutar el programa en python se siguen los siguientes pasos: 
 1. Descarga python en su página oficial o en Microsoft Store
 2. Descarga Visual Studio Code
 3. Ya con Visual Studio descargado se instala la extensión de python
 4. Crea una carpeta en tus archivos donde vayas a guardar tus códigos
 5. Abre la cartpeta y crea un archivo "Nombre.py", asegúrate de tener el ".py"

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
