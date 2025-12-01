# Carpeta /models/

Este directorio almacena los modelos entrenados por el motor de Machine Learning del proyecto.

## Archivos generados durante el entrenamiento

- `model_rf.pkl`  
  Modelo Random Forest supervisado para clasificación de tráfico IPv4.

- `autoencoder.h5`  
  Modelo Autoencoder no supervisado utilizado para la detección de anomalías mediante reconstrucción.

- `scaler.pkl`  
  Objeto StandardScaler usado para normalizar las características de entrada.

## Importante

Los archivos `.pkl` y `.h5` **no deben editarse manualmente**, ya que son binarios.

Deben generarse automáticamente ejecutando:

