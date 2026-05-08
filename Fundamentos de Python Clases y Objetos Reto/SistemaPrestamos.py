# =========================================
# SISTEMA DE PRÉSTAMOS DE EQUIPOS
# =========================================

# Importamos datetime para obtener la fecha actual
from datetime import datetime

# Diccionario principal del sistema
# Aquí almacenamos todos los equipos
# Cada equipo tiene:
# - disponible -> True o False
# - prestamos -> lista de préstamos
equipos = {
    "Laptop Dell": {
        "disponible": True,
        "prestamos": []
    },

    "Proyector Epson": {
        "disponible": True,
        "prestamos": []
    },

    "Tablet Samsung": {
        "disponible": True,
        "prestamos": []
    }
}


# =========================================
# FUNCIÓN PARA MOSTRAR LOS EQUIPOS
# =========================================
def mostrar_equipos():

    print("\n=== LISTA DE EQUIPOS ===")

    # Recorremos el diccionario
    for nombre, datos in equipos.items():

        # Operador ternario
        estado = "Disponible" if datos["disponible"] else "Prestado"

        # Mostramos nombre y estado
        print(f"- {nombre} -> {estado}")


# =========================================
# FUNCIÓN PARA REGISTRAR PRÉSTAMOS
# =========================================
def registrar_prestamo():

    print("\n=== REGISTRAR PRÉSTAMO ===")

    # Mostramos los equipos
    mostrar_equipos()

    # Pedimos el nombre del equipo
    equipo = input("\nIngrese el nombre exacto del equipo: ")

    # Verificamos si el equipo existe
    if equipo not in equipos:

        print("El equipo no existe.")
        return

    # Verificamos si el equipo está disponible
    if not equipos[equipo]["disponible"]:

        print("El equipo ya está prestado.")
        return

    # Pedimos el nombre del usuario
    usuario = input("Ingrese el nombre del usuario: ")

    # Obtenemos la fecha actual
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Creamos una tupla inmutable
    prestamo = (usuario, fecha)

    # Agregamos la tupla a la lista de préstamos
    equipos[equipo]["prestamos"].append(prestamo)

    # Cambiamos el estado del equipo
    equipos[equipo]["disponible"] = False

    print("Préstamo registrado correctamente.")


# =========================================
# FUNCIÓN PARA DEVOLVER EQUIPOS
# =========================================
def devolver_equipo():

    print("\n=== DEVOLVER EQUIPO ===")

    # Pedimos el nombre del equipo
    equipo = input("Ingrese el nombre exacto del equipo: ")

    # Verificamos si el equipo existe
    if equipo not in equipos:

        print("El equipo no existe.")
        return

    # Verificamos si el equipo ya está disponible
    if equipos[equipo]["disponible"]:

        print("El equipo ya se encuentra disponible.")
        return

    # Cambiamos el estado a disponible
    equipos[equipo]["disponible"] = True

    print("Equipo devuelto correctamente.")


# =========================================
# FUNCIÓN PARA VER EL HISTORIAL
# =========================================
def ver_historial():

    print("\n=== HISTORIAL DE PRÉSTAMOS ===")

    # Recorremos todos los equipos
    for nombre, datos in equipos.items():

        print(f"\nEquipo: {nombre}")

        # Verificamos si tiene préstamos
        if len(datos["prestamos"]) == 0:

            print("Sin préstamos registrados.")

        else:

            # Recorremos la lista de préstamos
            for usuario, fecha in datos["prestamos"]:

                print(f"Usuario: {usuario} | Fecha: {fecha}")


# =========================================
# FUNCIÓN PARA AGREGAR EQUIPOS
# =========================================
def agregar_equipo():

    print("\n=== AGREGAR NUEVO EQUIPO ===")

    # Pedimos el nombre del nuevo equipo
    nuevo_equipo = input("Ingrese el nombre del nuevo equipo: ")

    # Verificamos si ya existe
    if nuevo_equipo in equipos:

        print("El equipo ya existe.")
        return

    # Agregamos el nuevo equipo
    equipos[nuevo_equipo] = {
        "disponible": True,
        "prestamos": []
    }

    print("Equipo agregado correctamente.")


# =========================================
# FUNCIÓN PRINCIPAL DEL MENÚ
# =========================================
def menu():

    # Ciclo infinito
    while True:

        print("\n=================================")
        print(" SISTEMA DE PRÉSTAMOS DE EQUIPOS ")
        print("=================================")

        print("1. Ver equipos")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial")
        print("5. Agregar equipo")
        print("6. Salir")

        # Pedimos una opción
        opcion = input("Seleccione una opción: ")

        # Validamos la opción
        if opcion == "1":

            mostrar_equipos()

        elif opcion == "2":

            registrar_prestamo()

        elif opcion == "3":

            devolver_equipo()

        elif opcion == "4":

            ver_historial()

        elif opcion == "5":

            agregar_equipo()

        elif opcion == "6":

            print("Saliendo del sistema...")
            break

        else:

            print("Opción inválida. Intente nuevamente.")


# =========================================
# INICIO DEL PROGRAMA
# =========================================

# Verifica si el archivo se ejecuta directamente
if __name__ == "__main__":

    # Ejecutamos el menú principal
    menu()