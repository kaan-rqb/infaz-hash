# file_hash.py

import hashlib
import os

CHUNK_SIZE = 4096


def file_hash(file_path, algorithm="sha256"):
    """
    Dosyanın hash değerini hesaplar.
    """

    if not os.path.isfile(file_path):
        return None

    try:
        hash_obj = hashlib.new(algorithm)

        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(CHUNK_SIZE)

                if not chunk:
                    break

                hash_obj.update(chunk)

        return hash_obj.hexdigest()

    except ValueError:
        return None


def all_file_hashes(file_path):
    algorithms = [
        "md5",
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512"
    ]

    results = {}

    for algo in algorithms:
        results[algo.upper()] = file_hash(file_path, algo)

    return results


if __name__ == "__main__":

    file_path = input("Dosya yolu: ")

    if not os.path.exists(file_path):
        print("Dosya bulunamadı!")
        exit()

    print("\n=== DOSYA HASHLERİ ===\n")

    results = all_file_hashes(file_path)

    for algo, value in results.items():
        print(f"{algo}: {value}")
