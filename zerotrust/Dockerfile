FROM python:3.10-slim

WORKDIR /app

COPY zerotrust_service.py policy_engine.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "zerotrust_service:app", "--host", "0.0.0.0", "--port", "9000"]
