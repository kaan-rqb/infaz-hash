# compare.py

import os
from file_hash import file_hash

SUPPORTED_ALGORITHMS = [
    "md5",
    "sha1",
    "sha224",
    "sha256",
    "sha384",
    "sha512"
]


def compare_files(file1, file2, algorithm="sha256"):

    if algorithm not in SUPPORTED_ALGORITHMS:
        return {
            "success": False,
            "message": "Desteklenmeyen algoritma"
        }

    if not os.path.isfile(file1):
        return {
            "success": False,
            "message": f"Dosya bulunamadı: {file1}"
        }

    if not os.path.isfile(file2):
        return {
            "success": False,
            "message": f"Dosya bulunamadı: {file2}"
        }

    hash1 = file_hash(file1, algorithm)
    hash2 = file_hash(file2, algorithm)

    return {
        "success": True,
        "algorithm": algorithm.upper(),
        "file1_hash": hash1,
        "file2_hash": hash2,
        "same": hash1 == hash2
    }


def print_result(result):

    print("\n=== KARŞILAŞTIRMA SONUCU ===\n")

    if not result["success"]:
        print("[!] Hata:", result["message"])
        return

    print("Algoritma :", result["algorithm"])
    print("Dosya 1   :", result["file1_hash"])
    print("Dosya 2   :", result["file2_hash"])

    if result["same"]:
        print("\n[✓] Dosyalar aynı")
    else:
        print("\n[✗] Dosyalar farklı")


if __name__ == "__main__":

    print("=== DOSYA KARŞILAŞTIRICI ===\n")

    file1 = input("1. Dosya: ").strip()
    file2 = input("2. Dosya: ").strip()

    print("""
1 - MD5
2 - SHA1
3 - SHA224
4 - SHA256
5 - SHA384
6 - SHA512
""")

    choice = input("Seçim: ").strip()

    algos = {
        "1": "md5",
        "2": "sha1",
        "3": "sha224",
        "4": "sha256",
        "5": "sha384",
        "6": "sha512"
    }

    algorithm = algos.get(choice, "sha256")

    result = compare_files(file1, file2, algorithm)

    print_result(result)
