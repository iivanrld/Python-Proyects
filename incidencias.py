#!/usr/bin/env python3
"""
Ejercicio 4: Comando incidencia - Versión simple con fichero local
Se invoca desde línea de comandos: python incidencias.py "descripción"
Registra la incidencia en /tmp/incidencias.log (o incidencias.log en Windows)
con usuario, fecha, hora y descripción
"""

import sys
import os
from datetime import datetime

# Ruta del fichero log
# En sistemas tipo Unix: /tmp/incidencias.log
# En Windows: incidencias.log en el directorio actual
if os.name == 'posix':
    LOG_FILE = '/tmp/incidencias.log'
else:
    LOG_FILE = 'incidencias.log'

def registrar_incidencia(descripcion):
    """Registra una incidencia en el fichero log"""
    
    try:
        # Obtener nombre de usuario
        usuario = os.getenv('USERNAME') or os.getenv('USER') or 'usuario_desconocido'
        
        # Obtener fecha y hora actual
        ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Crear la línea con los datos
        linea = f"[{ahora}] Usuario: {usuario} | Incidencia: {descripcion}\n"
        
        # Escribir en el archivo (append mode para no sobrescribir)
        with open(LOG_FILE, 'a', encoding='utf-8') as archivo:
            archivo.write(linea)
        
        print(f"✓ Incidencia registrada correctamente")
        return True
        
    except IOError as e:
        print(f"✗ Error al registrar incidencia: {e}")
        return False

if __name__ == "__main__":
    # Verificar argumentos
    if len(sys.argv) < 2:
        # Si no hay argumentos, pedir interactivamente
        descripcion = input("Escribe la descripción de la incidencia: ").strip()
        if not descripcion:
            print("✗ La descripción no puede estar vacía")
            sys.exit(1)
    else:
        descripcion = sys.argv[1]
    
    # Registrar incidencia
    if registrar_incidencia(descripcion):
        print(f"Fichero log: {LOG_FILE}")
        sys.exit(0)
    else:
        sys.exit(1)
