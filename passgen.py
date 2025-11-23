#importamos las bibliotecas necesarias
import string
import random

longitud = int(input("Ingrese la longitud de la contraseña: "))

# Definimos el conjunto de caracteres a utilizar
caracteres = string.ascii_letters + string.digits + string.punctuation

# Generamos la contraseña
contraseña = "".join(random.choice(caracteres) for i in range(longitud))

# Mostramos la contraseña generada
print("Contraseña generada:", contraseña)