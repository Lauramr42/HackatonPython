'''
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%.
Escribe un programa que comience leyendo el número de barras vendidas que no son del día. 
Después tu programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace 
por no ser fresca y el coste final total.
'''
#definición de variables (precios)
precio = 3.49
descuento = 1 - 0.6
precioDescuento = precio * descuento

#preguntamos la cantidad de barras
numeroBarras=input("Introducir el número de barras vendidas que no son del día: ")
numeroBarras = int(numeroBarras)

#concatenar una cadena más un valor numérico CHOCA--> hay que convertir el número en string
print("Precio habitual: " + str(precio))
print("Descuento: "+str(round(precioDescuento,2)))
print("Coste final: "+ str(round(numeroBarras*precioDescuento)))

