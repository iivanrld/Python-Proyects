import socket

ip = input("Ingresa la direccion IP a escanear: ")

for puerto in range(1, 65535):
    # Crear un socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    # Intentar conectar a la ip y al puerto
    resultado = sock.connect_ex((ip, puerto))
    if resultado == 0:
        print(f"Puerto {puerto} está abierto")
    else:
        print(f"Puerto {puerto} está cerrado")
    sock.close()