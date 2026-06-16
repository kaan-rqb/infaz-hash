# folder_scan.py

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


def scan_folder(folder_path, algorithm="sha256"):

    if algorithm not in SUPPORTED_ALGORITHMS:
        return {
            "success": False,
            "message": "Desteklenmeyen algoritma."
        }

    if not os.path.isdir(folder_path):
        return {
            "success": False,
            "message": "Klasör bulunamadı."
        }

    results = []

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            full_path = os.path.join(root, file)

            try:
                size = os.path.getsize(full_path)

                hash_value = file_hash(
                    full_path,
                    algorithm
                )

                results.append({
                    "name": file,
                    "path": full_path,
                    "size": size,
                    "hash": hash_value
                })

            except Exception as e:

                results.append({
                    "name": file,
                    "path": full_path,
                    "size": 0,
                    "hash": "HATA",
                    "error": str(e)
                })

    return {
        "success": True,
        "algorithm": algorithm.upper(),
        "total_files": len(results),
        "results": results
    }


def print_results(data):

    if not data["success"]:
        print(f"\n[!] {data['message']}")
        return

    print("\n==============================")
    print("     KLASÖR TARAMA SONUCU")
    print("==============================")
    print(f"Algoritma : {data['algorithm']}")
    print(f"Dosya Sayısı : {data['total_files']}")
    print("==============================\n")

    for item in data["results"]:

        print(f"Dosya : {item['name']}")
        print(f"Boyut : {item['size']} Byte")
        print(f"Yol   : {item['path']}")
        print(f"Hash  : {item['hash']}")
        print("-" * 50)


if __name__ == "__main__":

    print("""
=================================
      INFXZ FOLDER SCANNER
=================================
""")

    folder = input("Klasör yolu: ").strip()

    print("""
1 - MD5
2 - SHA1
3 - SHA224
4 - SHA256
5 - SHA384
6 - SHA512
""")

    choice = input("Seçim: ").strip()

    algorithms = {
        "1": "md5",
        "2": "sha1",
        "3": "sha224",
        "4": "sha256",
        "5": "sha384",
        "6": "sha512"
    }

    algorithm = algorithms.get(choice, "sha256")

    result = scan_folder(
        folder,
        algorithm
    )

    print_results(result)
