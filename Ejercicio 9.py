#Ejercicio 9. Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

vNum= []

num1= (int) (input("Dime un número: \n"))
num2= (int) (input("Dime otro número: \n"))
num3= (int) (input("Dime otro número: \n"))

vNum.append(num1)
vNum.append(num2)
vNum.append(num3)
vNum.sort(reverse=True)

print(vNum)