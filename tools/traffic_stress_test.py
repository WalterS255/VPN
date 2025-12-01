import requests
import random
import time


def random_packet():
    return {
        "src_ip_int": random.randint(1, 2**32 - 1),
        "dst_ip_int": random.randint(1, 2**32 - 1),
        "ttl": random.randint(1, 128),
        "total_length": random.randint(60, 1500),
        "id": random.randint(0, 65535),
        "flags_mf": random.choice([0, 1]),
        "fragment_offset": random.randint(0, 200)
    }


def stress_test(n=200):
    url = "http://localhost:8000/predict"

    for i in range(n):
        packet = random_packet()
        r = requests.post(url, json=packet)

        print(f"[{i+1}/{n}] Estado: {r.status_code} | Respuesta: {r.json()}")
        time.sleep(0.05)  # 20 req/seg


if __name__ == "__main__":
    print("Iniciando prueba de estrés...")
    stress_test(200)
