#!/usr/bin/env python3
import socket
import sys
import struct

def cliente(ip_servidor, ruta_fichero):
    """Cliente que solicita ficheros al servidor"""
    
    puerto = 5000
    
    try:
        # Crear socket cliente
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conectar al servidor
        cliente_socket.connect((ip_servidor, puerto))
        
        # Enviar ruta del fichero solicitado (terminada con salto de línea)
        cliente_socket.sendall((ruta_fichero + '\n').encode('utf-8'))
        
        # Recibir tamaño del fichero (4 bytes, big-endian)
        tamaño_bytes = cliente_socket.recv(4)
        if len(tamaño_bytes) < 4:
            print("Error: Respuesta inválida del servidor")
            sys.exit(1)
        
        import struct
        tamaño = struct.unpack('>I', tamaño_bytes)[0]
        
        # Recibir contenido del fichero
        contenido = b""
        while len(contenido) < tamaño:
            datos = cliente_socket.recv(4096)
            if not datos:
                break
            contenido += datos
        
        # Mostrar contenido por pantalla
        try:
            print(contenido.decode('utf-8'), end='')
        except UnicodeDecodeError:
            # Si no es UTF-8, intentar con otra codificación o mostrar como bytes
            print("Error: No se pudo decodificar el fichero como texto UTF-8")
            sys.exit(1)
        
        cliente_socket.close()
        
    except ConnectionRefusedError:
        print(f"Error: No se puede conectar al servidor en {ip_servidor}:{puerto}")
        sys.exit(1)
    except socket.gaierror:
        print(f"Error: No se puede resolver la dirección {ip_servidor}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Verificar argumentos
    if len(sys.argv) != 3:
        print("Uso: python cliente.py <ip_servidor> <ruta_fichero>")
        print("Ejemplo: python cliente.py localhost /prac/trabajo.txt")
        exit()
    
    ip_servidor = sys.argv[1]
    ruta_fichero = sys.argv[2]
    
    cliente(ip_servidor, ruta_fichero)
