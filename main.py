#menu
import Funciones_parcial2
import os
ruta_archivo = os.path.join(os.getcwd(), "INVENTARIO.json")
while True:
    print("Menú de gestión de inventario:\n1. Crear Productos\n2. Mostrar productos\n3. Mostrar información de un producto\n4. Modificar producto\n5. Eliminar producto\n6.Salir")
    opcion=input("Ingrese una opción: ")
    if opcion=="1":
        respuesta_nombre=input("Nombre del producto: ")
        respuesta_precio=input("Precio del producto: ")
        respuesta_cantidad=input("cantidad del producto: ")
        Funciones_parcial2.agregar_producto(respuesta_nombre,respuesta_precio,respuesta_cantidad)
    elif opcion=="2":
        Funciones_parcial2.mostrar_productos(ruta_archivo)      
    elif opcion=="3":
            Funciones_parcial2.mostrar_productos(ruta_archivo)
            producto_buscado=input("ingrese el nombre por favor: ")
            Funciones_parcial2.buscar_producto(ruta_archivo,producto_buscado)
    elif opcion=="4":
        respuesta_nombre=input("Nombre del producto: ")
        respuesta_precio=input("Nuevo precio del producto: ")
        respuesta_cantidad=input("cantidad del producto actual: ")
        Funciones_parcial2.modificar_producto(respuesta_nombre,respuesta_precio,respuesta_cantidad)
    elif opcion=="5":
        Funciones_parcial2.mostrar_productos(ruta_archivo)
        print("Recordatorio al usuario: Los productos borrados para recuperarlos deben agregarse desde la opción 1\n")
        respuesta_nombre=input("Ingrese el nombre del producto a Eliminar: ")
        Funciones_parcial2.eliminar_producto(respuesta_nombre,ruta_archivo)
    elif opcion=="6":
        break
    else:
        print("ingrese el numero de una opción valida...por favor")