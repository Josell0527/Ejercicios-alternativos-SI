#Ejercicio 2. Algoritmo que pida un número y diga si es positivo, negativo o 0.
num1= 0
num1= (int)(input("Dime un número: \n"))
if (num1>0):
    print(f"{num1} es positivo")
else:
    if (num1<0):
        print (f"{num1} es negativo")
    else:
        if (num1==0):
           print("El número es 0")


