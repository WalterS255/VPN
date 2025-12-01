from fastapi import FastAPI
from pydantic import BaseModel
from policy_engine import evaluate_risk

app = FastAPI(title="Zero Trust Engine",
              description="Motor de políticas adaptativas Zero Trust",
              version="1.0")


class TrafficEvent(BaseModel):
    prediction: int
    score: float
    ttl: int
    fragment_offset: int
    flags_mf: int


@app.post("/evaluate")
def evaluate(event: TrafficEvent):
    """
    Procesa un evento de tráfico y determina acciones Zero Trust.
    """
    result = evaluate_risk(
        prediction=event.prediction,
        score=event.score,
        ttl=event.ttl,
        fragment_offset=event.fragment_offset,
        flags_mf=event.flags_mf
    )

    return result
