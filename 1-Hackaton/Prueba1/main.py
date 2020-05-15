'''
COMENTARIO EN BLOQUE--> entre puntos
COMENTARIO CON ALMOHADILLA #
'''
#definir variables
nombre = 'Manuel S. Lemos'
edad = 25
estaTrabajando = True # False 

#Sacar por pantalla
dato = input('Introduce un Dato ')
print(dato)

print(edad)
edad = edad + 1
print (edad)

#if--> sentencia acabada en ':'
if(edad >= 18):
    #para indicar que las sentencias van dentro del if TABULACIÓN
    nombre2 = input('Tu nombre: ')
    print(nombre2 + ' ' + 'eres mayor de edad')
else:
    print('Eres un crio')