"""
Archivo: main.py

Copyright (c) 2025 Demian Romero Bautista y Renata Garciía Resendiz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

Descripción: Punto de entrada principal de la aplicación Calculadora IP - CIDR y VLSM
Proyecto: Calculadora IP - CIDR y VLSM
Instituto Politécnico Nacional - Escuela Superior de Cómputo
Grupo: 5CV1
Asignatura: Redes de Computadoras
Fecha: Diciembre 2025

Instrucciones de ejecución:
    python main.py

Requisitos:
    - Python 3.7 o superior
    - Tkinter (incluido en Python estándar)

    ### 🤝 Contribuciones

Este proyecto fue desarrollado con fines educativos. Si encuentras errores 
o deseas mejorarlo, las contribuciones son bienvenidas mediante pull requests.

### 📞 Contacto

Para preguntas sobre este proyecto:
- Email del equipo: equipo.calculadora@gmail.com
- Repositorio: https://github.com/DemianRom/Calculadora-IP---CIDR-y-VLSM
- Issues: https://github.com/DemianRom/Calculadora-IP---CIDR-y-VLSM/issues

"""

import sys
import os

# Agregar el directorio src al path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Importar la interfaz gráfica
from gui import main as ejecutar_gui


def mostrar_banner():
    """
    Muestra el banner de bienvenida en consola.
    
    Observaciones:
        - Se muestra al iniciar la aplicación
        - Incluye información del proyecto
    """
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║            CALCULADORA IP - CIDR Y VLSM                   ║
    ║             Demian Romero Bautista y Renata Garcia Resendiz ║  
    ║                                                              ║
    ║            Instituto Politécnico Nacional                         ║
    ║            Escuela Superior de Cómputo                          ║
    ║                                                              ║
    ║            Proyecto 3: Calculadora IP                        ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    
    Iniciando aplicación...
    """
    print(banner)


def verificar_requisitos():
    """
    Verifica que todos los requisitos estén instalados.
    
    Salidas:
        bool: True si todos los requisitos están presentes
    
    Observaciones:
        - Verifica módulos necesarios
        - Muestra mensajes de error si falta algo
    """
    try:
        import tkinter
        return True
    except ImportError:
        print("ERROR: Tkinter no está instalado.")
        print("Tkinter viene incluido con Python en la mayoría de las instalaciones.")
        print("Si usa Linux, instale con: sudo apt-get install python3-tk")
        return False


def main():
    """
    Función principal de la aplicación.
    
    Descripción:
        - Muestra banner
        - Verifica requisitos
        - Inicia la interfaz gráfica
    
    Observaciones:
        - Maneja errores de inicialización
        - Proporciona mensajes claros al usuario
    """
    # Mostrar banner
    mostrar_banner()
    
    # Verificar requisitos
    if not verificar_requisitos():
        print("\nNo se puede iniciar la aplicación. Resuelva los problemas anteriores.")
        sys.exit(1)
    
    try:
        # Iniciar interfaz gráfica
        print("Abriendo interfaz gráfica...")
        ejecutar_gui()
        
    except KeyboardInterrupt:
        print("\n\nAplicación cerrada por el usuario.")
        sys.exit(0)
        
    except Exception as e:
        print(f"\n\nERROR FATAL: {str(e)}")
        print("\nDetalles del error:")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()