'''
Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la 
nota es mayor o igual a cinco, la edad es mayor o  igual a dieciocho y el sexo es ‘F’. En caso de que se 
cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones
 se debe mostrar ‘NO ACEPTADA’.
'''
nota= 0
edad= 0
sexo= ""
nota= (int)(input("Nota: \n"))
edad= (int)(input("Edad: \n"))
sexo= (input("Sexo, introduce M o F: \n"))
if(nota>=5 and edad>=18 and sexo=="F"):
 print("Aceptada")
if(nota>=5 and edad>=18 and sexo=="M"):
    print("Posible")
else:
    print("No aceptada")