#include <iostream> //Biblioteca que permite la entrada y salida de datos
using namespace std;

int c; //Variable que almacena el círculo en el que se encuentra
float t; //Variable que almacena el tiempo en el que estuvo en el círculo
int main (){
    //Se le pide al usuario que ingrese el numero del circulo en el que está 
    cout << "Escriba el círculo en el que se encuentra" << endl;
    cin >> c;
    //Se le pide al usuario que ingrese el tiempo en el que estuvo en el círculo
    cout << "Escriba el tiempo en el que estuvo en el círculo" << endl;
    cin >> t;

    //Se evalua en que circulo está el usuario 
    if(c==1){ 
        float a = 2*t; //Si el circulo es 1, se multiplica el tiempo por 2
        cout << "Daño total recibido: " << a << endl;//Se imprime el daño total recibido
    } else {
        if(c==2){
            float b = 5*t; //Si el circulo es 2, se multiplica el tiempo por 5
            cout << "Daño total recibido: " << b << endl;//Se imprime el daño total recibido
        } else {
            if(c==3){
                float d = 10*t; //Si el circulo es 3, se multiplica el tiempo por 10
                cout << "Daño total recibido: " << d << endl;//Se imprime el daño total recibido
            } else {
                if(c>=4){
                    float e = 25*t; //Si el circulo es 4 o mas, se multiplica el tiempo por 25
                    cout << "Daño total recibido: " << e << endl;//Se imprime el daño total recibido
                } else{
                    //Para casos en los que el circulo sea menor a 1
                    cout << "Usted no ha recibido daño";
                }
            }
        }
    }

return 0;
}
