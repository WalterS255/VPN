# 🔐 Sistema de Detección de Anomalías en Tráfico IPv4 dentro de VPN con Motor Zero Trust  
Proyecto Académico – Redes de Comunicación

Este proyecto implementa un sistema completo para la **detección de anomalías en tráfico IPv4 encapsulado dentro de una VPN**, utilizando:

- Aprendizaje automático (Random Forest)
- Autoencoder no supervisado
- Generación sintética de tráfico
- Motor Zero Trust para decisiones adaptativas
- Arquitectura desacoplada basada en contenedores
- Telemetría simulada
- API REST para inferencia en tiempo real

Todo el sistema es completamente funcional **sin hardware real**, mediante entornos simulados.

---

#  1. Objetivo del Proyecto

Diseñar e implementar un sistema capaz de:

1. Analizar metadatos del datagrama IPv4 (TTL, ID, offsets, fragmentación)  
2. Detectar anomalías incluso dentro de un túnel VPN cifrado  
3. Clasificar tráfico malicioso utilizando modelos de ML  
4. Ejecutar decisiones Zero Trust (permitir, desafiar, limitar o bloquear)  
5. Simular tráfico realista sin dispositivos físicos

Este repositorio contiene **el código, la arquitectura, la implementación y los modelos**.

---


