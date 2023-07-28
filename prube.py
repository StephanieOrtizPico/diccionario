def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado con éxito.")

def consultar_contacto(agenda, nombre):
    if nombre in agenda:
        telefono = agenda[nombre]
        print(f"Teléfono de {nombre}: {telefono}")
    else:
        print(f"No se encontró el contacto {nombre} en la agenda.")

def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"No se encontró el contacto {nombre} en la agenda.")

def mostrar_agenda(agenda):
    print("Agenda Telefónica:")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")
    print("------------------")

def main():
    agenda = {}

    while True:
        print("\n1. Agregar contacto")
        print("2. Consultar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar agenda")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            telefono = input("Ingrese el teléfono: ")
            agregar_contacto(agenda, nombre, telefono)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante a consultar: ")
            consultar_contacto(agenda, nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del estudiante a eliminar: ")
            eliminar_contacto(agenda, nombre)
        elif opcion == "4":
            mostrar_agenda(agenda)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida (1-5).")

if __name__ == "__main__":
    main()