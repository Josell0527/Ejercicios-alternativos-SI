#Ejercicio 9. Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
num1= 0
num2= 0
num3= 0

num1= (int) (input("Dime un número: \n"))
num2= (int) (input("Dime otro número: \n"))
num3= (int) (input("Dime otro número: \n"))

if (num1>num2 and num1>num3):
    mayor = num1

    if (num2>num3):
     mediano = num2
     menor = num3
    else:
     mediano = num3
     menor = num2
elif (num2>num1 and num2>num3):
    mayor = num2
    if (num1>num3):
     mediano = num1
     menor = num3
    else:
     mediano = num3
     menor = num1
else:
    mayor = num3
if (num2>num1):
    mediano = num2
    menor = num1
else:
     mediano = num1
     menor = num2

print(f"{mayor} > {mediano} > {menor}")