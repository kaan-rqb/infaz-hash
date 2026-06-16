

import hashlib


def md5_hash(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def sha1_hash(text):
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def sha224_hash(text):
    return hashlib.sha224(text.encode("utf-8")).hexdigest()


def sha256_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha384_hash(text):
    return hashlib.sha384(text.encode("utf-8")).hexdigest()


def sha512_hash(text):
    return hashlib.sha512(text.encode("utf-8")).hexdigest()


def all_hashes(text):
    return {
        "MD5": md5_hash(text),
        "SHA1": sha1_hash(text),
        "SHA224": sha224_hash(text),
        "SHA256": sha256_hash(text),
        "SHA384": sha384_hash(text),
        "SHA512": sha512_hash(text)
    }


if __name__ == "__main__":
    text = input("Metin Gir: ")

    results = all_hashes(text)

    print("\n=== HASH SONUÇLARI ===")
    for algo, value in results.items():
        print(f"{algo}: {value}")
