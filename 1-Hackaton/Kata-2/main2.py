'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al 
usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide 
con la guardada en la variable sin tener en cuenta mayúsculas y minúsuclas
'''
password="contraseña" 
passwordUsuario = input("Introducir la contraseña: ")
#Para poder comparar los valores y que no distinga entre mayúsculas y minúsculas usa lower
passwordUsuario = passwordUsuario.lower()

if password== passwordUsuario:
    print("Contraseña correcta")
else: 
    print("La contraseña no coincide")