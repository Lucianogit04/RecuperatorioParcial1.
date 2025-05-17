def mostrar_menu():
    print("-------------------------")
    print("\n🛒 MENÚ DE OPCIONES ")
    print("-------------------------")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")

def agregar_producto(productos, cantidades):
    nombre = input("\nIngrese el nombre del producto: ").strip()
    if nombre in productos:
        print("\nEste producto ya existe en el sistema.")
        return productos, cantidades
    
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible: "))
            if cantidad < 0:
                print("\nLa cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    productos.append(nombre)
    cantidades.append(cantidad)
    print(f"Producto '{nombre}' agregado exitosamente.")
    return productos, cantidades

def ver_productos_agotados(productos, cantidades):
    print("\n PRODUCTOS AGOTADOS:")
    hay_agotados = False
    for i in range(len(productos)):
        if cantidades[i] == 0:
            print(f"- {productos[i]}")
            hay_agotados = True
    
    if not hay_agotados:
        print("No hay productos agotados.")

def actualizar_stock(productos, cantidades):
    if not productos:
        print("\n No hay productos en el sistema.")
        return productos, cantidades
    
    print("\nPRODUCTOS DISPONIBLES:")
    for i in range(len(productos)):
        print(f"{i+1}. {productos[i]} (Stock actual: {cantidades[i]})")
    
    while True:
        try:
            indice = int(input("\nIngrese el número del producto a actualizar (0 para cancelar): ")) - 1
            if indice == -1:
                return productos, cantidades
            if 0 <= indice < len(productos):
                break
            print(" Número de producto inválido.")
        except ValueError:
            print(" Por favor, ingrese un número válido.")
    
    while True:
        try:
            nueva_cantidad = int(input(f"\nIngrese la nueva cantidad para {productos[indice]}: "))
            if nueva_cantidad < 0:
                print(" La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    cantidades[indice] = nueva_cantidad
    print(f" Stock de '{productos[indice]}' actualizado a {nueva_cantidad}.")
    return productos, cantidades

def ver_todos_productos(productos, cantidades):
    if not productos:
        print("\n No hay productos en el sistema.")
        return
    
    print("\n LISTADO COMPLETO DE PRODUCTOS:")
    print("-" * 40)
    print(f"{'PRODUCTO':<20} {'CANTIDAD':<10}")
    print("-" * 40)
    for i in range(len(productos)):
        print(f"{productos[i]:<20} {cantidades[i]:<10}")
    print("-" * 40)

def main():
    productos = []
    cantidades = []
    
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nSeleccione una opción (1-5): "))
            
            if opcion == 1:
                productos, cantidades = agregar_producto(productos, cantidades)
            elif opcion == 2:
                ver_productos_agotados(productos, cantidades)
            elif opcion == 3:
                productos, cantidades = actualizar_stock(productos, cantidades)
            elif opcion == 4:
                ver_todos_productos(productos, cantidades)
            elif opcion == 5:
                print("\nGracias por usar el sistema de gestión de stock")
                break
            else:
                print("\n Opción inválida. Por favor, seleccione una opción del 1 al 5.")
        except ValueError:
            print("\n Por favor, ingrese un número válido.")

if __name__ == "__main__":
    print("TECNICATURA DE PROGRAMACION A DISTANCIA")
    print("CONTRERAS LUCIANO DEMIAN")
    print("PROGRAMACION 1 : Recuperatorio")
    print("===========================================")
    print("         SISTEMA DE GESTIÓN DE STOCK       ")
    print("===========================================")
    main() 
