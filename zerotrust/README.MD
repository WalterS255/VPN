# Zero Trust Engine – Proyecto VPN + ML

Este módulo implementa el **motor Zero Trust** del sistema, con capacidad para:

- evaluar el nivel de riesgo de cada evento de tráfico  
- aplicar decisiones adaptativas (ALLOW, MFA, LIMIT, BLOCK)  
- complementar el análisis del motor ML  

---

## Endpoints

### `POST /evaluate`
Evalúa el riesgo de un paquete.

#### Ejemplo de entrada:
```json
{
  "prediction": 1,
  "score": 0.21,
  "ttl": 8,
  "fragment_offset": 120,
  "flags_mf": 1
}
