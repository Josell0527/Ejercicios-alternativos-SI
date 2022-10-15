'''
Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y 
el exponente. Pueden ocurrir tres cosas:
 El exponente sea positivo, sólo tienes que imprimir la potencia.
 El exponente sea 0, el resultado es 1.
 El exponente sea negativo, el resultado es 1/potencia con el exponente 
positivo.
'''
base= 0
exponente= 0

base= (int)(input("Dime la base de la potencia: \n"))
exponente= (int)(input("Dime el exponente de la potencia: \n"))
if (exponente>0):
    print(base**exponente)
if (exponente==0):
    print("El resultado es igual a 1")
if (exponente<0):
    print(1/(base**exponente))