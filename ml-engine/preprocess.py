import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib


def ip_to_int(ip):
    """Convierte una IP en un entero (formato apto para ML)."""
    parts = ip.split(".")
    return (
        int(parts[0]) * 256**3 +
        int(parts[1]) * 256**2 +
        int(parts[2]) * 256 +
        int(parts[3])
    )


def preprocess_dataset(path="dataset.csv", scaler_output="scaler.pkl"):
    print("[ML-ENGINE] Cargando dataset...")
    df = pd.read_csv(path)

    print("[ML-ENGINE] Convirtiendo IPs a enteros...")
    df["src_ip_int"] = df["src_ip"].apply(ip_to_int)
    df["dst_ip_int"] = df["dst_ip"].apply(ip_to_int)

    features = [
        "src_ip_int",
        "dst_ip_int",
        "ttl",
        "total_length",
        "id",
        "flags_mf",
        "fragment_offset"
    ]

    X = df[features].values
    y = df["label"].values

    print("[ML-ENGINE] Normalizando features...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    joblib.dump(scaler, scaler_output)
    print(f"[ML-ENGINE] Scaler guardado en: {scaler_output}")

    return X_scaled, y


if __name__
