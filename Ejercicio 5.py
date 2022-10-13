'''
Ejercicio 5. Escribe un programa que pida un nombre de usuario y una contraseña y si se haintroducido “pepe” y “asdasd” se indica
“Has entrado al sistema”, sino se da unerror.
'''
usuario =""
contra=""

usuario= input("Usuario: \n")
contra= input("Contraseña: \n")

if (usuario !="pepe"):
    print("Error")
elif (contra !="asdasd"):
    print("Error")
else: 
    print("Has entrado al sistema")
