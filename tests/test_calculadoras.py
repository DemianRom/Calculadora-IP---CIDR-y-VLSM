"""
Archivo: test_calculadoras.py

Copyright (c) 2025 Demian Romero Bautista y Renata Garciía Resendiz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.


Descripción: Tests unitarios para las calculadoras CIDR y VLSM
Grupo: 5CV1
Asignatura: Redes de Computadoras
Fecha: Diciembre 2025

Instrucciones para ejecutar:
    python -m pytest test_calculadoras.py -v

Nota: Requiere pytest instalado (pip install pytest)


"""

import sys
import os

# Agregar src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ip_utils import (
    validar_direccion_ip,
    validar_prefijo,
    ip_a_entero,
    entero_a_ip,
    prefijo_a_mascara,
    mascara_a_prefijo,
    calcular_direccion_red,
    calcular_broadcast,
    calcular_numero_hosts
)
from cidr_calculator import CalculadoraCIDR
from vlsm_calculator import CalculadoraVLSM


# ================================================================
# TESTS PARA IP_UTILS
# ================================================================

class TestIPUtils:
    """Tests para las funciones utilitarias de IP."""
    
    def test_validar_ip_valida(self):
        """Test: validar IPs válidas."""
        assert validar_direccion_ip("192.168.1.0") == True
        assert validar_direccion_ip("10.0.0.1") == True
        assert validar_direccion_ip("255.255.255.255") == True
        assert validar_direccion_ip("0.0.0.0") == True
    
    def test_validar_ip_invalida(self):
        """Test: rechazar IPs inválidas."""
        assert validar_direccion_ip("192.168.1.256") == False
        assert validar_direccion_ip("192.168.1") == False
        assert validar_direccion_ip("192.168.1.1.1") == False
        assert validar_direccion_ip("abc.def.ghi.jkl") == False
        assert validar_direccion_ip("") == False
    
    def test_validar_prefijo(self):
        """Test: validar prefijos."""
        assert validar_prefijo(0) == True
        assert validar_prefijo(16) == True
        assert validar_prefijo(24) == True
        assert validar_prefijo(32) == True
        assert validar_prefijo(33) == False
        assert validar_prefijo(-1) == False
    
    def test_conversion_ip_entero(self):
        """Test: conversión IP <-> entero."""
        # 192.168.1.0 = (192 << 24) + (168 << 16) + (1 << 8) + 0
        ip = "192.168.1.0"
        esperado = 3232235776
        assert ip_a_entero(ip) == esperado
        assert entero_a_ip(esperado) == ip
    
    def test_prefijo_a_mascara(self):
        """Test: conversión prefijo -> máscara."""
        assert prefijo_a_mascara(24) == "255.255.255.0"
        assert prefijo_a_mascara(16) == "255.255.0.0"
        assert prefijo_a_mascara(8) == "255.0.0.0"
        assert prefijo_a_mascara(30) == "255.255.255.252"
    
    def test_mascara_a_prefijo(self):
        """Test: conversión máscara -> prefijo."""
        assert mascara_a_prefijo("255.255.255.0") == 24
        assert mascara_a_prefijo("255.255.0.0") == 16
        assert mascara_a_prefijo("255.0.0.0") == 8
        assert mascara_a_prefijo("255.255.255.252") == 30
    
    def test_calcular_direccion_red(self):
        """Test: cálculo de dirección de red."""
        assert calcular_direccion_red("192.168.1.130", 24) == "192.168.1.0"
        assert calcular_direccion_red("10.5.7.200", 16) == "10.5.0.0"
        assert calcular_direccion_red("172.16.50.100", 20) == "172.16.48.0"
    
    def test_calcular_broadcast(self):
        """Test: cálculo de dirección de broadcast."""
        assert calcular_broadcast("192.168.1.0", 24) == "192.168.1.255"
        assert calcular_broadcast("10.0.0.0", 16) == "10.0.255.255"
        assert calcular_broadcast("192.168.0.0", 30) == "192.168.0.3"
    
    def test_calcular_numero_hosts(self):
        """Test: cálculo de número de hosts."""
        assert calcular_numero_hosts(24) == 254  # 2^8 - 2
        assert calcular_numero_hosts(16) == 65534  # 2^16 - 2
        assert calcular_numero_hosts(30) == 2  # 2^2 - 2
        assert calcular_numero_hosts(32) == 1  # Caso especial


# ================================================================
# TESTS PARA CALCULADORA CIDR
# ================================================================

class TestCalculadoraCIDR:
    """Tests para la Calculadora CIDR."""
    
    def setup_method(self):
        """Setup: crear instancia de calculadora antes de cada test."""
        self.calc = CalculadoraCIDR()
    
    def test_calcular_cidr_basico(self):
        """Test: caso básico CIDR /24."""
        resultado = self.calc.calcular("192.168.1.0/24")
        
        assert resultado['exito'] == True
        assert resultado['direccion_red'] == "192.168.1.0"
        assert resultado['broadcast'] == "192.168.1.255"
        assert resultado['primera_host'] == "192.168.1.1"
        assert resultado['ultima_host'] == "192.168.1.254"
        assert resultado['hosts_utilizables'] == 254
        assert resultado['mascara_decimal'] == "255.255.255.0"
    
    def test_calcular_cidr_con_mascara(self):
        """Test: CIDR con máscara decimal."""
        resultado = self.calc.calcular("192.168.1.0 255.255.255.0")
        
        assert resultado['exito'] == True
        assert resultado['prefijo'] == 24
        assert resultado['direccion_red'] == "192.168.1.0"
    
    def test_calcular_cidr_clase_a(self):
        """Test: red Clase A."""
        resultado = self.calc.calcular("10.0.0.0/8")
        
        assert resultado['exito'] == True
        assert resultado['direccion_red'] == "10.0.0.0"
        assert resultado['broadcast'] == "10.255.255.255"
        assert resultado['hosts_utilizables'] == 16777214  # 2^24 - 2
    
    def test_calcular_cidr_subred_pequena(self):
        """Test: subred /30 (punto a punto)."""
        resultado = self.calc.calcular("192.168.1.0/30")
        
        assert resultado['exito'] == True
        assert resultado['broadcast'] == "192.168.1.3"
        assert resultado['hosts_utilizables'] == 2
        assert resultado['primera_host'] == "192.168.1.1"
        assert resultado['ultima_host'] == "192.168.1.2"
    
    def test_entrada_invalida(self):
        """Test: manejo de entradas inválidas."""
        # IP inválida
        resultado = self.calc.calcular("192.168.1.256/24")
        assert resultado['exito'] == False
        
        # Prefijo inválido
        resultado = self.calc.calcular("192.168.1.0/33")
        assert resultado['exito'] == False
        
        # Formato incorrecto
        resultado = self.calc.calcular("no es una IP")
        assert resultado['exito'] == False
    
    def test_es_ip_privada(self):
        """Test: detección de IPs privadas."""
        assert self.calc.es_ip_privada("192.168.1.0") == True
        assert self.calc.es_ip_privada("10.0.0.0") == True
        assert self.calc.es_ip_privada("172.16.0.0") == True
        assert self.calc.es_ip_privada("172.20.0.0") == True
        assert self.calc.es_ip_privada("8.8.8.8") == False
        assert self.calc.es_ip_privada("1.1.1.1") == False
    
    def test_obtener_clase_ip(self):
        """Test: clasificación de IPs."""
        assert self.calc.obtener_informacion_clase("10.0.0.0") == "A"
        assert self.calc.obtener_informacion_clase("172.16.0.0") == "B"
        assert self.calc.obtener_informacion_clase("192.168.1.0") == "C"
        assert self.calc.obtener_informacion_clase("224.0.0.0") == "D (Multicast)"


# ================================================================
# TESTS PARA CALCULADORA VLSM
# ================================================================

class TestCalculadoraVLSM:
    """Tests para la Calculadora VLSM."""
    
    def setup_method(self):
        """Setup: crear instancia de calculadora antes de cada test."""
        self.calc = CalculadoraVLSM()
    
    def test_calcular_prefijo_requerido(self):
        """Test: cálculo de prefijo según hosts."""
        # 100 hosts → necesita 102 direcciones → log2(102) ≈ 6.67 → 7 bits → /25
        assert self.calc.calcular_prefijo_requerido(100) == 25
        
        # 50 hosts → necesita 52 direcciones → log2(52) ≈ 5.70 → 6 bits → /26
        assert self.calc.calcular_prefijo_requerido(50) == 26
        
        # 2 hosts → necesita 4 direcciones → log2(4) = 2 bits → /30
        assert self.calc.calcular_prefijo_requerido(2) == 30
        
        # 254 hosts → necesita 256 direcciones → log2(256) = 8 bits → /24
        assert self.calc.calcular_prefijo_requerido(254) == 24
    
    def test_ordenar_subredes(self):
        """Test: ordenamiento de subredes (mayor a menor)."""
        requisitos = [
            ("A", 50),
            ("B", 100),
            ("C", 25)
        ]
        
        ordenados = self.calc.ordenar_subredes(requisitos)
        
        assert ordenados[0] == ("B", 100)
        assert ordenados[1] == ("A", 50)
        assert ordenados[2] == ("C", 25)
    
    def test_vlsm_caso_basico(self):
        """Test: VLSM caso básico del documento."""
        red_base = "192.168.0.0/24"
        requisitos = [
            ("A", 100),
            ("B", 50),
            ("C", 25),
            ("D", 10)
        ]
        
        resultado = self.calc.calcular_vlsm(red_base, requisitos)
        
        assert resultado['exito'] == True
        assert len(resultado['subredes']) == 4
        
        # Verificar primera subred (la más grande)
        subred_a = resultado['subredes'][0]
        assert subred_a.nombre == "A"
        assert subred_a.hosts_requeridos == 100
        assert subred_a.red == "192.168.0.0"
        assert subred_a.prefijo == 25  # /25 da 126 hosts
        
        # Verificar que no hay solapamiento
        redes = [s.red for s in resultado['subredes']]
        assert len(redes) == len(set(redes))  # Todas únicas
    
    def test_vlsm_espacio_insuficiente(self):
        """Test: manejo de error cuando no hay espacio."""
        red_base = "192.168.0.0/24"
        requisitos = [
            ("Grande", 500)  # Requiere más de 256 direcciones
        ]
        
        resultado = self.calc.calcular_vlsm(red_base, requisitos)
        
        assert resultado['exito'] == False
        assert 'insuficiente' in resultado['error'].lower()
    
    def test_vlsm_subredes_contiguas(self):
        """Test: verificar que las subredes son contiguas."""
        red_base = "192.168.1.0/24"
        requisitos = [
            ("A", 60),
            ("B", 30)
        ]
        
        resultado = self.calc.calcular_vlsm(red_base, requisitos)
        
        assert resultado['exito'] == True
        
        # Primera subred debe empezar en .0
        assert resultado['subredes'][0].red == "192.168.1.0"
        
        # Segunda subred debe empezar justo después de la primera
        # A: 60 hosts → /26 (64 direcciones) → ocupa 192.168.1.0-63
        # B: debe empezar en 192.168.1.64
        assert resultado['subredes'][1].red == "192.168.1.64"
    
    def test_vlsm_eficiencia(self):
        """Test: cálculo de eficiencia."""
        red_base = "192.168.0.0/24"
        requisitos = [
            ("A", 100),
            ("B", 50)
        ]
        
        resultado = self.calc.calcular_vlsm(red_base, requisitos)
        
        assert resultado['exito'] == True
        assert 'eficiencia' in resultado
        assert 0 <= resultado['eficiencia'] <= 100
        
        # Hosts requeridos = 150
        # A: 126 hosts (/25), B: 62 hosts (/26) = 188 hosts asignados
        # Eficiencia = 150/188 * 100 ≈ 79.79%
        assert resultado['eficiencia'] > 75
        assert resultado['eficiencia'] < 85
    
    def test_validar_requisitos(self):
        """Test: validación previa de requisitos."""
        red_base = "192.168.0.0/24"
        
        # Requisitos válidos
        req_validos = [("A", 50), ("B", 30)]
        validacion = self.calc.validar_requisitos(red_base, req_validos)
        assert validacion['valido'] == True
        
        # Requisitos inválidos (host negativo)
        req_invalidos = [("A", -10)]
        validacion = self.calc.validar_requisitos(red_base, req_invalidos)
        assert validacion['valido'] == False
        
        # Espacio insuficiente
        req_grandes = [("Grande", 300)]
        validacion = self.calc.validar_requisitos(red_base, req_grandes)
        assert validacion['valido'] == False


# ================================================================
# TESTS DE CASOS ESPECÍFICOS DEL PROYECTO
# ================================================================

class TestCasosProyecto:
    """Tests basados en los casos de prueba del documento."""
    
    def test_caso_cidr_documento(self):
        """Test: caso de prueba CIDR del documento."""
        calc = CalculadoraCIDR()
        resultado = calc.calcular("192.168.10.0/24")
        
        assert resultado['direccion_red'] == "192.168.10.0"
        assert resultado['primera_host'] == "192.168.10.1"
        assert resultado['ultima_host'] == "192.168.10.254"
        assert resultado['broadcast'] == "192.168.10.255"
    
    def test_caso_vlsm_documento(self):
        """Test: caso de prueba VLSM del documento."""
        calc = CalculadoraVLSM()
        red_base = "192.168.0.0/24"
        requisitos = [
            ("A", 100),
            ("B", 50),
            ("C", 25),
            ("D", 10)
        ]
        
        resultado = calc.calcular_vlsm(red_base, requisitos)
        
        assert resultado['exito'] == True
        assert len(resultado['subredes']) == 4
        
        # Verificar que se asignaron correctamente
        nombres = [s.nombre for s in resultado['subredes']]
        assert "A" in nombres
        assert "B" in nombres
        assert "C" in nombres
        assert "D" in nombres


# ================================================================
# INSTRUCCIONES PARA EJECUTAR
# ================================================================

"""
EJECUCIÓN DE TESTS:

1. Instalar pytest:
   pip install pytest pytest-cov

2. Ejecutar todos los tests:
   python -m pytest test_calculadoras.py -v

3. Ejecutar con cobertura:
   python -m pytest test_calculadoras.py --cov=src --cov-report=html

4. Ejecutar un test específico:
   python -m pytest test_calculadoras.py::TestIPUtils::test_validar_ip_valida -v

5. Ver reporte de cobertura:
   Abrir htmlcov/index.html en navegador

RESULTADOS ESPERADOS:
- Todos los tests deben pasar (verde)
- Cobertura debe ser > 90%
- No debe haber warnings críticos
"""

if __name__ == "__main__":
    print("Ejecute los tests con: python -m pytest test_calculadoras.py -v")