# Calculadora IP - CIDR y VLSM

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![IPN-ESCOM](https://img.shields.io/badge/IPN-ESCOM-green.svg)](https://www.escom.ipn.mx/)

> Herramienta de subredes IPv4 (CIDR/VLSM) construida con Python.

## 📚 Información del Proyecto

**Institución:** Instituto Politécnico Nacional - Escuela Superior de Cómputo  
**Proyecto:** Proyecto 3 - Calculadora IP: CIDR y VLSM  
**Materia:** Redes de Computadoras  
**Fecha:** Diciembre 2025  

## 📖 Descripción

Aplicación de escritorio en Python que proporciona dos herramientas para el cálculo y diseño de redes IP:

1. **Calculadora CIDR:** Calcula subredes, rangos de hosts, direcciones broadcast y máscaras de subred.
2. **Calculadora VLSM:** Subdivide redes en subredes de tamaño variable según requisitos específicos de hosts.

## 💻 Requisitos

- Python 3.7 o superior
- Tkinter (incluido en instalaciones estándar de Python)
- Sistema Operativo: Windows, Linux o macOS

## 🚀 Instalación y Ejecución

### 1. Verificar Python
```bash
python --version
```

### 2. Clonar el repositorio
```bash
git clone https://github.com/DemianRom/Calculadora-IP---CIDR-y-VLSM.git
cd Calculadora-IP---CIDR-y-VLSM
```

### 3. Ejecutar la aplicación

**Opción 1 - Python directo:**
```bash
python main.py
```

**Opción 2 - Windows:**
```bash
ejecutar_win.bat
```

**Opción 3 - Linux/Mac:**
```bash
chmod +x ejecutar_mac.sh
./ejecutar_mac.sh
```

##  Estructura del Proyecto

```
calculadora-ip-vlsm/
├── src/
│   ├── __init__.py
│   ├── ip_utils.py              # Utilidades para manejo de IPs
│   ├── cidr_calculator.py       # Lógica de la calculadora CIDR
│   ├── vlsm_calculator.py       # Lógica de la calculadora VLSM
│   └── gui.py                   # Interfaz gráfica
├── docs/
│   └── screenshot.png
├── main.py                      # Punto de entrada
├── README.md
├── requirements.txt
├── ejecutar_win.bat
└── ejecutar_mac.sh
```

## Algoritmo VLSM

El algoritmo implementado sigue estos pasos:

1. **Validación de entrada:** Parsear y validar red base (IP/prefijo)
2. **Cálculo de espacio:** `espacio_total = 2^(32 - prefijo_base)`
3. **Preparación:** Agregar 2 hosts por red/broadcast y ordenar por tamaño (mayor → menor)
4. **Asignación de subredes:**
   - Calcular prefijo: `mask_bits = 32 - ceil(log2(hosts_necesarios))`
   - Calcular tamaño: `2^(32 - mask_bits)`
   - Asignar direcciones y avanzar puntero
5. **Validación:** Verificar que no se exceda el espacio disponible

### Ejemplo

**Red Base:** `192.168.1.0/24`

**Requisitos:**
- Ventas: 50 hosts → `/26` (64 hosts) → `192.168.1.0/26`
- Administración: 25 hosts → `/27` (32 hosts) → `192.168.1.64/27`
- IT: 10 hosts → `/28` (16 hosts) → `192.168.1.96/28`

## 🔧 Solución de Problemas

### Error: "No module named 'tkinter'"
**Linux:**
```bash
sudo apt-get install python3-tk
```

### Error: "No se puede encontrar el módulo src"
```bash
cd /ruta/a/calculadora-ip-vlsm
python main.py
```

### Error: "Espacio insuficiente" en VLSM
Usar una red base más grande (ej: cambiar de `/24` a `/23`)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## Agradecimientos

- Instituto Politécnico Nacional
- Escuela Superior de Cómputo
- Profesor: Juan Jesus Alcaráz Torres

---

**"La Técnica al Servicio de la Patria"**