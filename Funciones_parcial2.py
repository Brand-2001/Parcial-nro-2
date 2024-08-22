import json
import os
ruta_archivo = os.path.join(os.getcwd(), "INVENTARIO.json")

def agregar_producto(producto, precio, cantidad):
    with open(ruta_archivo, 'r+') as f:
        data= json.load(f)
        data.append({"producto": producto, "precio": precio, "cantidad": cantidad})
        f.seek(0)
        json.dump(data, f, indent=4)
        print(f"Se ha agregado el producto {producto}.")

def modificar_producto(producto, nuevo_precio, nueva_cantidad):
    try:
#Leer el archivo JSON existente
        with open(ruta_archivo, 'r') as f:
            data = json.load(f)

#Crear una copia de los datos
        copia_seguridad = data.copy()

#Encontrar y modificar el producto (si existe)
        for i, item in enumerate(data):
            if item['producto'] == producto:
                data[i]['precio'] = nuevo_precio
                data[i]['cantidad'] = nueva_cantidad
                break

#Sobrescribir el archivo con la lista modificada
        with open(ruta_archivo, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Se han actualizado los datos del producto {producto}.")

    except json.JSONDecodeError as e:
        print(f"Error al parsear el archivo JSON: {e}")
    except FileNotFoundError:
        print("El archivo INVENTARIO.json no existe.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        print("Restaurando los datos desde la copia de seguridad...")
        with open(ruta_archivo, 'w') as f:
            json.dump(copia_seguridad, f, indent=4)

#agregar_producto("Mandarindo", 3.5, 11)
#modificar_producto("Mango", 3, 13)

def eliminar_producto(producto, ruta_archivo):
    try:
#Leer el archivo json
        with open(ruta_archivo, 'r') as f:
            data = json.load(f)

#Crear una copia de los datos
        copia_seguridad = data.copy()

#Filtrar la lista para eliminar el producto
        data = [item for item in data if item['producto'] != producto]

#Sobrescribir el archivo con la lista filtrada
        with open(ruta_archivo, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Se han eliminado el producto con el nombre '{producto}'.")

    except json.JSONDecodeError as e:
        print(f"Error al parsear el archivo json: {e}")
    except FileNotFoundError:
        print("El archivo INVENTARIO.json no existe.")

    # Si ocurre algún error, restaurar los datos
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        print("Restaurando los datos desde la copia de seguridad...")
        with open(ruta_archivo, 'w') as f:
            json.dump(copia_seguridad, f, indent=4)

#eliminar_producto("Mandarindo", ruta_archivo)

def mostrar_productos(ruta_archivo):

    try:
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)

        if datos:
            print("Productos en el inventario:")
            for i, producto in enumerate(datos, start=1):
                print(f"{i}. {producto['producto']}")
        else:
            print("El inventario está vacío.")

    except FileNotFoundError:
        print(f"No se encontró el archivo {ruta_archivo}")
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON: {e}")

#mostrar_productos(ruta_archivo)

def buscar_producto(ruta_archivo, producto_a_buscar):

    with open(ruta_archivo, 'r') as archivo:
        datos = json.load(archivo)

        for producto in datos:
            if producto['producto'] == producto_a_buscar:
                print(f"Producto: {producto['producto']}")
                print(f"Precio: {producto['precio']}")
                print(f"Cantidad: {producto['cantidad']}")
                return  
 # Terminamos la función al encontrar el producto buscado
        print(f"No se encontró el producto {producto_a_buscar}.")

#producto_a_buscar = "Naranja"
#buscar_producto(ruta_archivo, producto_a_buscar)