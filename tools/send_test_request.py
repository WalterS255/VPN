import requests
import random
import time


def random_packet():
    """Genera un paquete sintético con características IPv4."""
    return {
        "src_ip_int": random.randint(1, 2**32 - 1),
        "dst_ip_int": random.randint(1, 2**32 - 1),
        "ttl": random.randint(1, 128),
        "total_length": random.randint(60, 1500),
        "id": random.randint(0, 65535),
        "flags_mf": random.choice([0, 1]),
        "fragment_offset": random.randint(0, 200)
    }


def send():
    url = "http://localhost:8000/predict"

    sample = random_packet()
    print("Enviando muestra:", sample)

    response = requests.post(url, json=sample)

    print("Respuesta del modelo:")
    print(response.json())


if __name__ == "__main__":
    send()
