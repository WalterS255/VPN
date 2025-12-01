def evaluate_risk(prediction, score, ttl, fragment_offset, flags_mf):
    """
    Motor de reglas Zero Trust basado en:
    - predicción del modelo ML
    - score de anomalía (autoencoder)
    - características sensibles del paquete
    """

    risk = 0
    reasons = []

    # -----------------------------------------
    # Basado en ML
    # -----------------------------------------
    if prediction == 1:
        risk += 60
        reasons.append("El modelo clasificó el paquete como anómalo.")

    if score > 0.15:
        risk += 30
        reasons.append("La reconstrucción del autoencoder fue alta (indicador de anomalía).")

    # -----------------------------------------
    # Basado en features críticas
    # -----------------------------------------
    if ttl <= 10:
        risk += 15
        reasons.append("TTL extremadamente bajo.")

    if fragment_offset > 50:
        risk += 20
        reasons.append("Offset inusualmente alto o solapado (posible ataque).")

    if flags_mf == 1 and fragment_offset > 0:
        risk += 10
        reasons.append("Fragmentación activa.")

    # Normalizar
    risk = min(risk, 100)

    # -----------------------------------------
    # Acciones Zero Trust
    # -----------------------------------------
    if risk < 30:
        action = "ALLOW"
    elif risk < 60:
        action = "CHALLENGE_MFA"
    elif risk < 85:
        action = "LIMIT_PRIVILEGES"
    else:
        action = "BLOCK"

    return {
        "risk_score": risk,
        "action": action,
        "reasons": reasons
    }
