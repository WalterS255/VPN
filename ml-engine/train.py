import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from preprocess import preprocess_dataset
from tensorflow import keras
from tensorflow.keras import layers


# ============================================================
# Modelo Autoencoder no supervisado
# ============================================================

def build_autoencoder(input_dim):
    inputs = keras.Input(shape=(input_dim,))
    encoded = layers.Dense(16, activation="relu")(inputs)
    encoded = layers.Dense(8, activation="relu")(encoded)

    decoded = layers.Dense(16, activation="relu")(encoded)
    outputs = layers.Dense(input_dim, activation="linear")(decoded)

    autoencoder = keras.Model(inputs, outputs)
    autoencoder.compile(optimizer="adam", loss="mse")

    return autoencoder


# ============================================================
# Entrenamiento completo
# ============================================================

def train_models():
    print("[ML-ENGINE] Preprocesando dataset...")
    X_scaled, y = preprocess_dataset()

    # ------------------- Random Forest ------------------------
    print("[ML-ENGINE] Entrenando Random Forest...")
    rf = RandomForestClassifier(
        n_estimators=150,
        max_depth=12,
        class_weight="balanced"
    )
    rf.fit(X_scaled, y)

    joblib.dump(rf, "model_rf.pkl")
    print("[ML-ENGINE] Modelo Random Forest guardado: model_rf.pkl")

    # Métricas
    preds = rf.predict(X_scaled)
    print("\n=== REPORT Random Forest ===")
    print(classification_report(y, preds))

    # ------------------- Autoencoder --------------------------
    print("[ML-ENGINE] Entrenando Autoencoder...")
    input_dim = X_scaled.shape[1]
    autoencoder = build_autoencoder(input_dim)

    autoencoder.fit(
        X_scaled,
        X_scaled,
        epochs=20,
        batch_size=32,
        verbose=1
    )

    autoencoder.save("autoencoder.h5")
    print("[ML-ENGINE] Autoencoder guardado: autoencoder.h5")


if __name__ == "__main__":
    train_models()
