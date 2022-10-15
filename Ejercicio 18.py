#Ejercicio 18. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día 
#correspondiente. Si introducimos otro número nos da un error
num= 0
num= (int)(input("Dime un número del 1 al 7: \n"))
if (num==1):
    print("Día: Lunes")
if (num==2):
    print("Día: Martes")
if (num==3):
    print("Día: Miércoles")
if (num==4):
    print("Día: Jueves")
if (num==5):
    print("Día: Viernes")
if (num==6):
    print("Día: Sábado")
if (num==7):
    print("Día: Domingo")
if(num>=8):
    print("Error")
