#Ejercicio 4. Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.
num1= 0
num2= 0

num1= (int)(input("Dime un número: \n"))
num2= (int)(input("Dime otro número: \n"))
if (num2 == 0):
    print("La división no se puede realizar")
else:
    print(f"{num1} / {num2}: ", num1/num2)