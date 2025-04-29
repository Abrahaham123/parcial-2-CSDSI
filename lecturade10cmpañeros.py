try:
    with open("compañero.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())
except FileNotFoundError:
    print("El archivo no existe. Asegúrate de que 'compañero.txt' esté en la carpeta correcta.")
