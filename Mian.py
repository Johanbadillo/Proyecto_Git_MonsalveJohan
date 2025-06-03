# #######################################
# ######### Proyecto git prueba #########
# #####################################
from Funciones.funciones import *
salida=True

while(salida):
    print("Bienvenido a nuestro programa de empanadas Doña Pepa\
        \n\
        \n=====================================\
        \n           Menu Principal             \
        \n======================================\
        \nGestion de Datos:\
        \n1. Agregar dato nuevo\
        \n2. Editar dato\
        \n3. Eliminar dato\
        \n4. Salir")
    Opcion=int(input("Ingrese una opcion numerica\n"))
    if(Opcion==1):
        Nombre=str(input("Ingrese el nombre de la empanada: "))
        precio=int(input("Ingrese el precio de la empanada sin puntos ni comas: "))
        Caningredientes=int(input("Ingrese la cantidad de ingredientes que tiene la empanada: "))
        diccionarioNuevo={
            "nombre":Nombre,
            "precio":precio,
            "ingredientes":[]
        }
        for i in range (Caningredientes):
            nomIngrediente=str(input("Ingrese el nombre del ingrediente: "))
            disponibilidad=int(input("¿El ingrediente esta disponible?\n1. Si\n2. No\nIngrese una opcion numerica "))
            if(disponibilidad==1):
                disponible=str('si')
            else:
                disponible=str('no')
        















# Pruebas 
