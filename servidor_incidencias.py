#!/usr/bin/env python3
"""
Servidor de incidencias - Recibe y registra incidencias de múltiples clientes (Ejercicio 3)
Escucha en puerto 3333 y registra incidencias en fichero log con IP origen
Formato recibido: usuario|hora|descripción
"""

import socket
import os
from datetime import datetime

# Ruta del fichero log (compatible con Windows y Linux)
LOG_FILE = "incidencias.log"

def registrar_incidencia(usuario, hora, descripcion, ip_origen):
    """Registra la incidencia en el archivo log con IP origen"""
    
    # Crear la línea con los datos completos
    linea = f"[{hora}] IP: {ip_origen} | Usuario: {usuario} | Incidencia: {descripcion}\n"
    
    # Escribir en el archivo (append mode para no sobrescribir)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as archivo:
            archivo.write(linea)
        return True
    except Exception as e:
        print(f"✗ Error al escribir en log: {e}")
        return False

def iniciar_servidor(puerto=3333):
    """Inicia el servidor de incidencias en el puerto 3333"""
    
    # Crear socket
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Permitir reutilizar el puerto si está en TIME_WAIT
    servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Vincular el socket a todas las interfaces (0.0.0.0) y al puerto
    try:
        servidor_socket.bind(('0.0.0.0', puerto))
        print(f"✓ Servidor iniciado en puerto {puerto}")
        print(f"  Fichero de log: {os.path.abspath(LOG_FILE)}")
    except OSError as e:
        print(f"✗ Error al vincular el puerto {puerto}: {e}")
        return
    
    # Escuchar conexiones (máximo 5 conexiones en espera)
    servidor_socket.listen(5)
    print("Esperando incidencias de clientes...\n")
    
    try:
        while True:
            # Aceptar conexión
            conexion, (ip_cliente, puerto_cliente) = servidor_socket.accept()
            print(f"✓ Conexión desde {ip_cliente}:{puerto_cliente}")
            
            try:
                # Recibir datos de la incidencia
                # Formato: usuario|hora|descripción
                datos = conexion.recv(1024).decode('utf-8').strip()
                
                if not datos:
                    print("  ⚠ Datos vacíos recibidos")
                    conexion.send("ERROR: Datos vacíos".encode('utf-8'))
                    continue
                
                # Parsear datos
                partes = datos.split('|', 2)  # Máximo 3 partes
                
                if len(partes) != 3:
                    print(f"  ⚠ Formato incorrecto: {datos}")
                    conexion.send("ERROR: Formato incorrecto".encode('utf-8'))
                    continue
                
                usuario, hora, descripcion = partes
                
                # Registrar en log
                exito = registrar_incidencia(usuario, hora, descripcion, ip_cliente)
                
                if exito:
                    print(f"  Usuario: {usuario}")
                    print(f"  Hora: {hora}")
                    print(f"  Descripción: {descripcion}")
                    # Enviar confirmación
                    conexion.send("OK".encode('utf-8'))
                else:
                    conexion.send("ERROR: No se pudo registrar".encode('utf-8'))
                
            except Exception as e:
                print(f"  ✗ Error al procesar incidencia: {e}")
                try:
                    conexion.send(f"ERROR: {str(e)}".encode('utf-8'))
                except:
                    pass
            finally:
                conexion.close()
                print()
    
    except KeyboardInterrupt:
        print("\n✓ Servidor detenido por el usuario")
    finally:
        servidor_socket.close()
        print("Fichero de incidencias:")
        print("=" * 70)
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                print(f.read())
        print("=" * 70)

if __name__ == "__main__":
    iniciar_servidor()
