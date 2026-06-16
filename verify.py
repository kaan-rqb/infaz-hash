# verify.py

from file_hash import file_hash
import os


def verify_hash(file_path, expected_hash, algorithm="sha256"):
    """
    Dosyanın hash değerini doğrular.
    """

    if not os.path.isfile(file_path):
        return False, "Dosya bulunamadı."

    calculated_hash = file_hash(file_path, algorithm)

    if calculated_hash is None:
        return False, "Geçersiz algoritma."

    if calculated_hash.lower() == expected_hash.lower():
        return True, calculated_hash

    return False, calculated_hash


if __name__ == "__main__":

    print("=== HASH DOĞRULAMA ===\n")

    file_path = input("Dosya yolu: ")
    algorithm = input(
        "Algoritma (md5, sha1, sha224, sha256, sha384, sha512): "
    ).lower()

    expected_hash = input("Beklenen hash: ")

    result, data = verify_hash(
        file_path,
        expected_hash,
        algorithm
    )

    print()

    if result:
        print("[✓] Hash doğrulandı!")
        print(f"Hash: {data}")
    else:
        print("[✗] Hash eşleşmedi!")
        print(f"Hesaplanan: {data}")
