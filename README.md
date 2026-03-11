# 🔐 Portfolio Python - Security Tools

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Una colección de herramientas de seguridad e información desarrolladas en Python**

[Características](#-características) • [Instalación](#-instalación) • [Uso](#-uso) • [Herramientas](#-herramientas)

</div>

---

## 🎯 Características

✨ **Herramientas versátiles** - Múltiples utilidades de seguridad e información  
⚡ **Fácil de usar** - Interfaz interactiva por línea de comandos  
🔒 **Seguridad** - Algoritmos criptográficos estándar  
📦 **Ligero** - Mínimas dependencias externas  
🚀 **Optimizado** - Código eficiente y bien documentado  

---

## 📋 Herramientas

### 🔓 Hash Cracker
**Archivo:** [`hashcracker.py`](hashcracker.py)

Descifrador de contraseñas usando ataques de diccionario contra hashes SHA256.

```
┌─────────────────────────────────────┐
│  Ingresa archivo de diccionario     │
│  Compara hashes SHA256              │
│  Encuentra la contraseña coincidente│
└─────────────────────────────────────┘
```

**Flujo:**
1. Define un hash SHA256 objetivo
2. Lee un diccionario de contraseñas
3. Genera hash SHA256 de cada palabra
4. Compara con el hash objetivo
5. Muestra resultado si encuentra coincidencia

**Ejemplo de uso:**
```bash
python hashcracker.py
# Ingresa la dirección del archivo de diccionario: diccionario.txt
# Contraseña encontrada: micontraseña
```

**⚠️ Nota:** Ideal para auditorías autorizadas y pruebas de seguridad.

---

### 🔐 Password Generator
**Archivo:** [`passgen.py`](passgen.py)

Generador de contraseñas aleatorias personalizables con caracteres especiales.

```
┌─────────────────────────────────────┐
│  Solicita longitud deseada          │
│  Genera contraseña aleatoria        │
│  Incluye mayúsculas, minúsculas,    │
│  números y caracteres especiales    │
└─────────────────────────────────────┘
```

**Características:**
- 🔤 Letras mayúsculas y minúsculas
- 🔢 Números (0-9)
- 🎯 Caracteres especiales (!@#$%^&*)
- 📏 Longitud personalizable

**Ejemplo de uso:**
```bash
python passgen.py
# Ingrese la longitud de la contraseña: 16
# Contraseña generada: K7#mP@9xL2$qR4&w
```

---

### 🌐 Port Scanner
**Archivo:** [`portscanner.py`](portscanner.py)

Escáner de puertos TCP para identificar servicios activos en una máquina.

```
┌─────────────────────────────────────┐
│  Solicita dirección IP              │
│  Escanea puertos 1-65535            │
│  Identifica puertos abiertos        │
│  Muestra estado de cada puerto      │
└─────────────────────────────────────┘
```

**Funcionalidad:**
- 🔍 Escaneo completo de puertos
- ⏱️ Timeout configurable (0.5s)
- 📊 Detección de puertos abiertos/cerrados
- 🎯 Información en tiempo real

**Ejemplo de uso:**
```bash
python portscanner.py
# Ingresa la dirección IP a escanear: 192.168.1.1
# Puerto 22 está abierto
# Puerto 80 está abierto
# Puerto 443 está abierto
```

**💡 Tip:** Usar solo en redes autorizadas. Los puertos comunes son:
- **22** → SSH
- **80** → HTTP
- **443** → HTTPS
- **3306** → MySQL

---

### 📱 QR Code Generator
**Archivo:** [`qr.py`](qr.py)

Generador de códigos QR a partir de URLs, configurables y descargables.

```
┌─────────────────────────────────────┐
│  Define URL/contenido               │
│  Genera código QR                   │
│  Guarda como imagen PNG             │
│  ¡Listo para usar!                  │
└─────────────────────────────────────┘
```

**Características:**
- 🎨 Imagen PNG de alta calidad
- 🔗 Soporte para URLs
- 📦 Personalizable (tamaño, borde)
- 💾 Guardado automático

**Ejemplo de uso:**
```bash
python qr.py
# Se genera: instagram_qr.png
```

**Resultado:** Código QR listo para compartir en redes sociales 📲

---

### 📤 Protocolo de Compartición de Ficheros
**Archivos:** [`servidor.py`](servidor.py) y [`cliente.py`](cliente.py)

Sistema cliente-servidor para compartir ficheros a través de sockets TCP/IP. Perfecto para transferir archivos entre máquinas en la misma red o de forma remota.

```
┌─────────────────────────────────────┐
│  Cliente solicita fichero           │
│  Servidor busca en directorio       │
│  Valida acceso seguro               │
│  Envía contenido del fichero        │
└─────────────────────────────────────┘
```

**Características:**
- 🔐 Validación de seguridad (previene path traversal)
- 📡 Protocolo robusto con tamaño de archivo
- 🚀 Transferencia binaria eficiente
- ⚡ Manejo de errores completo
- 💻 Funciona en Windows, Linux y macOS

**Componentes:**

**Servidor:**
```bash
python servidor.py <ruta-del-directorio-a-compartir>
```

**Cliente:**
```bash
python cliente.py <ip-servidor> <ruta-relativa-fichero>
```

**Ejemplo de uso:**

Terminal 1 (Servidor):
```bash
$ python servidor.py "c:\Users\usuario\compartido"
Estas compartiendo la carpeta c:\Users\usuario\compartido ...
Nos piden el fichero c:\Users\usuario\compartido\prac\trabajo.txt ...
```

Terminal 2 (Cliente):
```bash
$ python cliente.py localhost /prac/trabajo.txt
TITULO DE FICHERO
Este es el contenido del fichero que has pedido.
Un fichero de texto normal y corriente
```

**Protocolo de Comunicación:**
1. Cliente envía ruta del fichero (terminada con `\n`)
2. Servidor responde con tamaño en 4 bytes (big-endian)
3. Servidor envía el contenido del fichero
4. Cliente muestra el contenido en pantalla

**Uso en red:**
```bash
# En otra máquina (IP: 192.168.1.100)
python cliente.py 192.168.1.100 /documentos/archivo.txt
```

**Limitaciones:**
- ⚠️ Sin autenticación
- ⚠️ Sin encriptación
- ⚠️ Procesa conexiones secuencialmente
- ℹ️ Ficheros en modo UTF-8

---

### 📋 Sistema de Incidencias
**Archivos:** 
- **Ejercicio 4 (Local):** [`Incidencias/incidencias.py`](Incidencias/incidencias.py)
- **Ejercicio 3 (Red):** [`Incidencias/servidor_incidencias.py`](Incidencias/servidor_incidencias.py) y [`Incidencias/cliente_incidencias.py`](Incidencias/cliente_incidencias.py)

Sistema completo para registrar y gestionar incidencias en dos versiones: local y distribuida.

```
┌─────────────────────────────────────┐
│  Usuario registra incidencia        │
│  Obtiene usuario, fecha y hora      │
│  Opción 1: Guarda en fichero local  │
│  Opción 2: Envía a servidor central │
└─────────────────────────────────────┘
```

#### **Ejercicio 4: Incidencias Locales**

Comando que registra incidencias en un fichero log local.

**Características:**
- ✅ Se invoca desde línea de comandos
- ✅ Obtiene automáticamente el nombre de usuario
- ✅ Registra fecha y hora exacta
- ✅ Acumula registros (no sobrescribe)
- ✅ Compatible Windows y Linux

**Uso:**
```bash
# Modo 1: Con argumento
python Incidencias/incidencias.py "Mi sesión sufre desconexiones periódicas"

# Modo 2: Interactivo (sin argumentos)
python Incidencias/incidencias.py
# Escribe la descripción de la incidencia: Mi sesión sufre desconexiones
```

**Formato del fichero log:**
```
[2026-03-11 14:30:45] Usuario: usuario1 | Incidencia: Mi sesión sufre desconexiones
[2026-03-11 14:35:20] Usuario: usuario2 | Incidencia: No puedo acceder al servidor
[2026-03-11 15:00:10] Usuario: usuario1 | Incidencia: Impresora no funciona
```

#### **Ejercicio 3: Incidencias por Red (Cliente-Servidor)**

Ampliación con arquitectura distribuida. Las incidencias se envían a un servidor central que las registra con IP origen.

**Servidor:**
```bash
python Incidencias/servidor_incidencias.py
```

**Cliente:**
```bash
python Incidencias/cliente_incidencias.py "descripción de la incidencia"
```

**Características:**
- 🌐 Arquitectura cliente-servidor
- 📡 Comunicación por sockets TCP en puerto 3333
- 🔍 Registro de IP origen de cada incidencia
- ✅ Confirmación de recepción del servidor
- 💼 Ideal para sistemas empresariales/distribuidos

**Ejemplo completo:**

Terminal 1 (Servidor):
```bash
$ python Incidencias/servidor_incidencias.py
✓ Servidor iniciado en puerto 3333
  Fichero de log: C:\ruta\incidencias.log
Esperando incidencias de clientes...

✓ Conexión desde 127.0.0.1:54321
  Usuario: usuario1
  Hora: 2026-03-11 14:30:45
  Descripción: Mi sesión sufre desconexiones
```

Terminal 2 (Cliente):
```bash
$ python Incidencias/cliente_incidencias.py "Mi sesión sufre desconexiones"
✓ Incidencia registrada correctamente
```

**Formato del fichero log con servidor:**
```
[2026-03-11 14:30:45] IP: 127.0.0.1 | Usuario: usuario1 | Incidencia: Mi sesión sufre desconexiones
[2026-03-11 14:35:20] IP: 192.168.1.100 | Usuario: usuario2 | Incidencia: No puedo acceder al servidor
```

**Protocolo:**
- Formato de mensaje: `usuario|hora|descripción`
- Respuesta servidor: `OK` o `ERROR`
- Puerto: 3333 (configurable)

**Uso en red remota:**
```bash
# Cliente en otra máquina conectando a servidor central
python Incidencias/cliente_incidencias.py "Mi problema" "192.168.1.100"
```

**Comparación:**

| Aspecto | Ejercicio 4 | Ejercicio 3 |
|---------|-----------|-----------|
| **Tipo** | Local | Distribuida |
| **Almacenamiento** | Fichero local | Servidor centralizado |
| **Registro IP** | ❌ | ✅ |
| **Alcance** | Una máquina | Red completa |
| **Escalabilidad** | Baja | Alta |
| **Validación** | ❌ | ✅ |

---

## 🚀 Instalación

### Requisitos previos
- Python 3.8 o superior
- pip (gestor de paquetes)

### Pasos de instalación

1. **Clona el repositorio**
```bash
git clone https://github.com/tu-usuario/portfolio-python.git
cd portfolio-python
```

2. **Crea un entorno virtual (opcional pero recomendado)**
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

3. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

---

## 📦 Dependencias

Crea un archivo `requirements.txt`:

```txt
qrcode[pil]==7.4.2
```

---

## 💻 Uso

### Opción 1: Ejecutar directamente
```bash
python hashcracker.py
python passgen.py
python portscanner.py
python qr.py
```

### Opción 2: Protocolo de Compartición de Ficheros

**Iniciar servidor:**
```bash
# En Terminal 1
python servidor.py "C:\ruta\del\directorio"
```

**Solicitar fichero (en otra Terminal o máquina):**
```bash
# En Terminal 2
python cliente.py localhost /ruta/relativa/fichero.txt
```

**Ejemplo completo:**
```bash
# Terminal 1 - Servidor
$ python servidor.py "C:\Users\usuario\compartido"
Estas compartiendo la carpeta C:\Users\usuario\compartido ...

# Terminal 2 - Cliente
$ python cliente.py localhost /documento.txt
# Muestra el contenido del fichero
```

### Opción 3: Sistema de Incidencias

**Versión Local (Ejercicio 4):**
```bash
python Incidencias/incidencias.py "descripción de la incidencia"
```

**Versión Red (Ejercicio 3):**
```bash
# Terminal 1 - Servidor
python Incidencias/servidor_incidencias.py

# Terminal 2 - Cliente (o máquina diferente)
python Incidencias/cliente_incidencias.py "descripción de la incidencia"
```

### Opción 4: Menú interactivo (opcional)
Crea un `main.py` para facilitar el uso:

```bash
python main.py
```

---

## ⚙️ Configuración

### Personalizar Hash Cracker
Edita `hashcracker.py` para cambiar el hash objetivo:

```python
hash_file = "tu_hash_aqui"  # Reemplaza con tu hash
```

### Personalizar QR Generator
Modifica la URL en `qr.py`:

```python
url = "https://tu-url.com"  # Cambia la URL
```

### Ajustar Port Scanner
Modifica el rango de puertos en `portscanner.py`:

```python
for puerto in range(1, 1000):  # Escanea solo puertos comunes
```

### Configurar Protocolo de Compartición
Personaliza el puerto y opciones en `servidor.py` y `cliente.py`:

**Cambiar puerto (por defecto 5000):**
```python
# En servidor.py
puerto = 5000  # Cambia a cualquier puerto disponible

# En cliente.py
puerto = 5000  # Debe ser el mismo que el servidor
```

**Usar en otra red:**
```bash
# Reemplaza "localhost" con la IP del servidor
python cliente.py 192.168.1.100 /fichero.txt
```

### Configurar Sistema de Incidencias

**Cambiar puerto del servidor (por defecto 3333):**
```python
# En Incidencias/servidor_incidencias.py
iniciar_servidor(3333)  # Cambia a cualquier puerto disponible
```

**Cambiar ruta del fichero log:**
```python
# En Incidencias/incidencias.py (Ejercicio 4)
LOG_FILE = '/tmp/incidencias.log'  # Para Linux/Mac
LOG_FILE = 'C:\\logs\\incidencias.log'  # Para Windows

# En Incidencias/servidor_incidencias.py (Ejercicio 3)
LOG_FILE = "ruta/del/fichero/incidencias.log"
```

---

## 📊 Estadísticas

| Herramienta | Líneas | Dependencias | Complejidad |
|-------------|--------|--------------|-------------|
| hashcracker.py | 14 | 1 (hashlib) | Baja |
| passgen.py | 12 | 2 (string, random) | Muy baja |
| portscanner.py | 14 | 1 (socket) | Media |
| qr.py | 10 | 1 (qrcode) | Baja |
| servidor.py | 68 | 3 (socket, os, struct) | Media |
| cliente.py | 52 | 3 (socket, sys, struct) | Media |
| incidencias.py | 48 | 3 (sys, os, datetime) | Baja |
| servidor_incidencias.py | 95 | 3 (socket, os, datetime) | Media |
| cliente_incidencias.py | 63 | 4 (socket, sys, os, datetime) | Baja |

---

## 🔒 Consideraciones de Seguridad

⚠️ **Uso responsable:**
- Usa estas herramientas solo en sistemas que posees o con autorización
- El Port Scanning no autorizado puede ser ilegal
- El Hash Cracking debe realizarse solo para auditoría personal
- Nunca compartas diccionarios o hashes sensibles
- El sistema de incidencias no incluye autenticación (agrégala en producción)

✅ **Buenas prácticas:**
- Realiza auditorías de seguridad autorizadas
- Documenta todos tus escaneos e incidencias
- Usa en entornos de laboratorio primero
- Cumple con las leyes locales
- Protege los ficheros de incidencias (contienen datos sensibles)

---

## 📈 Futuras mejoras

- [ ] Interfaz gráfica (GUI)
- [ ] Soporte para otros algoritmos hash (MD5, SHA512)
- [ ] Base de datos de resultados
- [ ] Escaneo asincrónico de puertos
- [ ] Validación de entrada mejorada
- [ ] Logging de eventos
- [ ] Autenticación para protocolo de compartición (usuario/contraseña)
- [ ] Encriptación SSL/TLS para servidor-cliente
- [ ] Listado de directorios remotos
- [ ] Manejo de múltiples conexiones simultáneas
- [ ] Interfaz GUI para compartición de ficheros
- [ ] Soporte para descarga de múltiples ficheros
- [ ] Autenticación para sistema de incidencias
- [ ] Base de datos centralizada para incidencias
- [ ] Búsqueda y filtrado de incidencias
- [ ] Notificaciones en tiempo real

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit cambios (`git commit -m 'Añade mejora'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 👨‍💻 Autor

**Iván Roldán**

- Instagram: [@iivan_rld](https://www.instagram.com/iivan_rld/)
- GitHub: [iivanrld](https://github.com/iivanrld)

---

## 📞 Soporte

¿Tienes preguntas o encontraste un bug?

- Abre un [Issue](../../issues)
- Contacta directamente por Instagram

---

<div align="center">

**⭐ Si te fue útil, no olvides dejar una estrella ⭐**

Hecho con ❤️ usando Python

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python)

</div>
