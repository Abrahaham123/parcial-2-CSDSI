print("Bienvenido al registro de usuarios")

nombre = input("Por favor, escribe tu nombre completo: ")
while nombre.strip() == "":
    print("El nombre no puede estar vacío.")
    nombre = input("Intenta de nuevo: ")

print("Ahora ingresa tu fecha de nacimiento")
dia = input("Día (dd): ")
mes = input("Mes (mm): ")
ano = input("Año (aaaa): ")

fecha = dia + "/" + mes + "/" + ano

linea_a_guardar = nombre + "," + fecha + "\n"

archivo = open("usuarios.txt", "a")
archivo.write(linea_a_guardar)
archivo.close()

print("\nGracias, tus datos han sido guardados correctamente.")
