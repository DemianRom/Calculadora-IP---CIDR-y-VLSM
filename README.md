# Calculadora IP - CIDR y VLSM

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![IPN-ESCOM](https://img.shields.io/badge/IPN-ESCOM-green.svg)](https://www.escom.ipn.mx/)
[GitHub stars](https://img.shields.io/github/stars/DemianRom/Calculadora-IP---CIDR-y-VLSM?style=social)](https://github.com/DemianRom/Calculadora-IP---CIDR-y-VLSM/stargazers)

> Herramienta robusta de subredes IPv4 (CIDR/VLSM) construida con Python. 
> Creada para estudios de Ingeniería en Redes y código abierto bajo licencia MIT.

## Información del Proyecto

**Institución:** Instituto Politécnico Nacional - Escuela Superior de Cómputo  
**Proyecto:** Proyecto 3 - Calculadora IP: CIDR y VLSM  
**Fecha:** Diciembre 2025  

## Descripción

Aplicación de escritorio desarrollada en Python que proporciona dos herramientas fundamentales para el cálculo y diseño de redes IP:

1. Calculadora CIDR: Calcula subredes, rangos de hosts, direcciones broadcast y máscaras de subred.
2. **Calculadora VLSM**: Subdivide redes en subredes de tamaño variable según requisitos específicos de hosts.

## Requisitos del Sistema
- **Python:** 3.7 o superior
- **Sistema Operativo:** Windows, Linux o macOS
- **Dependencias:** Tkinter (incluido en instalaciones estándar de Python)


## Ejecución

### Forma 1: ecutar directamente

```bash
python main.py
```

### Forma 2: Usando el script ejecutable (Windows)

Hacer doble clic en `ejecutar.bat`

### Forma 3: Usando el script ejecutable (Linux/Mac)

```bash
chmod +x ejecutar.sh
./ejecutar.sh
```

## Estructura del Proyecto

```
calculadora-ip-vlsm/
│
├── src/
│   ├── ip_utils.py              # Utilidades para manejo de IPs
│   ├── cidr_calculator.py       # Lógica de la calculadora CIDR
│   ├── vlsm_calculator.py       # Lógica de la calculadora VLSM
│   └── gui.py                   # Interfaz gráfica de usuario
├── docs/
│   └──screenshot.png       
│
├── main.py                       # Punto de entrada de la aplicación
├── README.md                     # Este archivo
├── ejecutar_win.bat          # Script para Windows
├── ejecutar_mac.sh            # Script para Linux/Mac
└── requirements.txt             # Dependencias del proyecto


```


## Solución de Problemas

### Problema: "ModuleNotFoundError: No module named 'tkinter'"
**Solución (Linux):**
```bash
sudo apt-get install python3-tk
```

### Problema: "No se puede encontrar el módulo src"
**Solución:**
Asegurarse de ejecutar desde el directorio raíz del proyecto:
```bash
cd /ruta/a/calculadora-ip-vlsm
python main.py
```

### Problema: Ventana no se muestra
**Solución:**
Verificar que el sistema tenga entorno gráfico y soporte para Tkinter.

# =====================================================
# INSTRUCCIONES DE USO
# =====================================================

INSTALACIÓN Y EJECUCIÓN:

1. Asegúrese de tener Python 3.7+ instalado:
   python --version

2. Extraiga todos los archivos manteniendo la estructura:
   calculadora-ip-vlsm/
   ├── src/
   │   ├── __init__.py
   │   ├── ip_utils.py
   │   ├── cidr_calculator.py
   │   ├── vlsm_calculator.py
   │   └── gui.py
   ├── main.py
   ├── ejecutar.bat (Windows)
   └── ejecutar.sh (Linux/Mac)

3. WINDOWS: Doble clic en "ejecutar.bat"
   LINUX/MAC: En terminal: ./ejecutar.sh
   O directamente: python main.py


ESTRUCTURA DE ARCHIVOS:
- main.py: Punto de entrada
- src/: Contiene toda la lógica
  - ip_utils.py: Funciones de conversión y validación de IPs
  - cidr_calculator.py: Lógica de cálculo CIDR
  - vlsm_calculator.py: Lógica de cálculo VLSM
  - gui.py: Interfaz gráfica
- README.md: Documentación completa
- requirements.txt: Dependencias
- ejecutar.bat/.sh: Scripts de ejecución


# =====================================================
## Algoritmo VLSM Explicado
# =====================================================

El algoritmo VLSM implementado sigue estos pasos:

1. **Validación de entrada:**
   - Parsear red base (IP/prefijo)
   - Validar que la IP y el prefijo sean correctos

2. **Cálculo de espacio disponible:**
   - Espacio total = 2^(32 - prefijo_base)

3. **Preparación de requisitos:**
   - Para cada requisito, calcular hosts_necesarios = hosts_requeridos + 2
   - Ordenar requisitos por hosts_necesarios (mayor → menor)

4. **Asignación de subredes:**
   - Para cada requisito:
     - Calcular prefijo: mask_bits = 32 - ceil(log2(hosts_necesarios))
     - Calcular tamaño del bloque: 2^(32 - mask_bits)
     - Asignar dirección de red = puntero_actual
     - Calcular primera_host = red + 1
     - Calcular última_host = red + tamaño - 2
     - Calcular broadcast = red + tamaño - 1
     - Avanzar puntero: puntero_actual += tamaño

5. **Validación:**
   - Verificar que puntero_actual no exceda el límite de la red base
   - Si excede → Error: "Espacio insuficiente"

##  Equipo de Desarrollo

Este proyecto fue desarrollado por estudiantes de:

**Instituto Politécnico Nacional**  
**Escuela Superior de Cómputo**  
Proyecto 3 - Redes de Computadoras

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver LICENSE para más detalles.

## 🙏 Agradecimientos

- Instituto Politécnico Nacional
- Escuela Superior de Cómputo
- Profesor: [Juan Jesus Alcaráz Torres]

---

**"La Técnica al Servicio de la Patria"**
