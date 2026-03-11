#!/usr/bin/env python3
import socket
import sys
import os
import struct

def servidor(directorio_compartido):
    """Servidor que comparte ficheros de un directorio específico"""
    
    # Crear socket servidor
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind al puerto 5000 en todas las interfaces
    puerto = 5000
    servidor_socket.bind(('0.0.0.0', puerto))
    servidor_socket.listen(5)
    
    print(f"Estas compartiendo la carpeta {directorio_compartido} ...")
    
    try:
        while True:
            # Aceptar conexión de cliente
            conexion, dirección = servidor_socket.accept()
            
            try:
                # Recibir ruta del fichero solicitado (terminada con \n)
                ruta_fichero = ""
                while True:
                    char = conexion.recv(1).decode()
                    if char == '\n' or not char:
                        break
                    ruta_fichero += char
                
                # Construir ruta completa (segura)
                ruta_completa = os.path.normpath(
                    os.path.join(directorio_compartido, ruta_fichero.lstrip('/').lstrip('\\'))
                )
                
                # Verificar que la ruta está dentro del directorio compartido
                ruta_compartido = os.path.normpath(directorio_compartido)
                if not ruta_completa.startswith(ruta_compartido):
                    raise ValueError("Intento de acceso fuera del directorio compartido")
                
                print(f"Nos piden el fichero {ruta_completa} ...")
                
                # Leer fichero
                with open(ruta_completa, 'rb') as f:
                    contenido = f.read()
                
                # Enviar tamaño del fichero (4 bytes, big-endian)
                import struct
                tamaño = len(contenido)
                conexion.sendall(struct.pack('>I', tamaño))
                
                # Enviar contenido
                conexion.sendall(contenido)
                
            except FileNotFoundError:
                import struct
                mensaje = b"ERROR: Fichero no encontrado"
                conexion.sendall(struct.pack('>I', len(mensaje)))
                conexion.sendall(mensaje)
            except Exception as e:
                import struct
                mensaje = f"ERROR: {str(e)}".encode('utf-8')
                conexion.sendall(struct.pack('>I', len(mensaje)))
                conexion.sendall(mensaje)
            finally:
                conexion.close()
                
    except KeyboardInterrupt:
        print("\nServidor detenido")
    finally:
        servidor_socket.close()

if __name__ == "__main__":
    # Verificar argumentos
    if len(sys.argv) < 2:
        # Usar directorio actual por defecto
        directorio = os.getcwd()
        print(f"No se especificó directorio. Usando directorio actual: {directorio}")
    else:
        directorio = sys.argv[1]
    
    # Verificar que el directorio existe
    if not os.path.isdir(directorio):
        print(f"Error: {directorio} no es un directorio válido")
        sys.exit(1)
    
    # Convertir a ruta absoluta
    directorio = os.path.abspath(directorio)
    
    servidor(directorio)
