#Ejercicio 3. Escribe un programa que lea un número e indique si es par o impar.
num1= 0

num1= (int)(input("Dime un número: \n"))
if (num1%2 !=0):
    print(f"{num1} es impar")
else:
    print(f"{num1} es par")