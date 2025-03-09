#include <iostream> //Biblioteca que permite la entrada y salida de datos

int c; //Variable que almacena el círculo en el que se encuentra
float t; //Variable que almacena el tiempo en el que estuvo en el círculo
int main (){
    //Se le pide al usuario que ingrese el numero del circulo en el que está 
    std::cout << "Escriba el círculo en el que se encuentra" << std::endl;
    std::cin >> c;
    //Se le pide al usuario que ingrese el tiempo en el que estuvo en el círculo
    std::cout << "Escriba el tiempo en segundos en el que estuvo en el círculo" << std::endl;
    std::cin >> t;
    //Se evalúa que el tiempo ingresado ssea coherente
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
