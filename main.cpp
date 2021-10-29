#include <iostream>

using namespace std;

template < class TIPOA>
void mostrarNumero (TIPOA numero);
int main() {
	int num1=10;
	float num2=100.50;
	double num3=120.5047;
	
	mostrarNumero(num1);
	mostrarNumero(num2);
	mostrarNumero(num3);
	
	return 0;
}

template <class TIPOA>
void mostrarNumero (TIPOA numero){
	if(numero<0){
		numero= numero*-1;
		
	}
	cout<<"El valor absoluto es : "<<numero<<endl;
	
}