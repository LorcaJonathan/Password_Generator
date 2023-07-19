import random
import string

def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password
try:
    while True:
        cantidad_contraseñas = input("Indica la cantidad de contraseñas que quieres generar -> ")

        if cantidad_contraseñas.isdigit():
            cantidad_contraseñas = int(cantidad_contraseñas)
            break
        else:
            print("¡Error! La cantidad de contraseñas debe ser un número entero. Inténtalo nuevamente.")

    while True:
        longitud = input("Ingrese la longitud deseada para la contraseña -> ")

        if longitud.isdigit():
            longitud = int(longitud)
            break
        else:
            print("¡Error! La cantidad de contraseñas debe ser un número entero. Inténtalo nuevamente.")

    passwords_generadas = []
    for _ in range(cantidad_contraseñas):
        password_generada = generar_password(longitud)
        passwords_generadas.append(password_generada)

    print("-- Contraseñas generadas --")
    for numero, contraseña in enumerate(passwords_generadas, start=1):
        print(f"Contraseña Nº{numero} -> {contraseña}")
except KeyboardInterrupt:
    print("\nCerrando Script...")