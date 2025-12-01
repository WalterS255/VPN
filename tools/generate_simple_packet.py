import random


def benign():
    return {
        "src_ip_int": random.randint(1, 2**32 - 1),
        "dst_ip_int": random.randint(1, 2**32 - 1),
        "ttl": random.randint(50, 128),
        "total_length": random.randint(60, 1500),
        "id": random.randint(0, 65535),
        "flags_mf": random.choice([0, 1]),
        "fragment_offset": random.choice([0, 0, 0, random.randint(1, 5)])
    }


def ttl_low():
    return {
        "src_ip_int": random.randint(1, 2**32 - 1),
        "dst_ip_int": random.randint(1, 2**32 - 1),
        "ttl": random.randint(1, 10),
        "total_length": random.randint(60, 1500),
        "id": random.randint(0, 65535),
        "flags_mf": 0,
        "fragment_offset": 0
    }


def fragment_overlap():
    return {
        "src_ip_int": random.randint(1, 2**32 - 1),
        "dst_ip_int": random.randint(1, 2**32 - 1),
        "ttl": random.randint(20, 60),
        "total_length": random.randint(300, 1500),
        "id": random.randint(0, 65535),
        "flags_mf": 1,
        "fragment_offset": random.randint(20, 200)
    }


def id_repetition():
    rid = random.randint(0, 65535)
    return {
        "src_ip_int": random.randint(1, 2**32 - 1),
        "dst_ip_int": random.randint(1, 2**32 - 1),
        "ttl": random.randint(30, 90),
        "total_length": random.randint(60, 1500),
        "id": rid,
        "flags_mf": 0,
        "fragment_offset": 0
    }


if __name__ == "__main__":
    print("Benigno:", benign())
    print("TTL Bajo:", ttl_low())
    print("Overlap:", fragment_overlap())
    print("ID Repetido:", id_repetition())
