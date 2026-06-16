# main.py

import os
from termcolor import colored

from hashes import all_hashes
from file_hash import all_file_hashes
from verify import verify_hash
from compare import compare_files
from folder_scan import scan_folder
from history import show_history
from logs import show_logs
from settings import settings_menu

BANNER = r"""

  \ | __| \ \ / __ / | | \ __| | |
. | _| > < / ____| __ | _ \ \__ \ __ |
_|\_| _| _/\_\ ____| _| _| _/ _\ ____/ _| _|

        INFXZ HASH TOOL
          by Infxz Team

"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def success(msg):
    print(colored(f"[+] {msg}", "green"))


def error(msg):
    print(colored(f"[-] {msg}", "red"))


def warning(msg):
    print(colored(f"[!] {msg}", "yellow"))


def info(msg):
    print(colored(f"[*] {msg}", "cyan"))


def show_menu():

    print(colored(BANNER, "red"))

    print(colored("╔══════════════════════════════╗", "red"))
    print(colored("║         ANA MENÜ            ║", "red"))
    print(colored("╚══════════════════════════════╝", "red"))

    print(colored("[1]", "green"), "Metin Hashle")
    print(colored("[2]", "green"), "Dosya Hashle")
    print(colored("[3]", "green"), "Hash Doğrula")
    print(colored("[4]", "green"), "Dosya Karşılaştır")
    print(colored("[5]", "green"), "Klasör Tara")
    print(colored("[6]", "green"), "Geçmiş")
    print(colored("[7]", "green"), "Loglar")
    print(colored("[8]", "green"), "Ayarlar")
    print(colored("[0]", "red"), "Çıkış")


while True:

    clear()
    show_menu()

    secim = input(
        colored("\nSeçim > ", "cyan")
    )

    if secim == "1":

        text = input("\nMetin: ")

        sonuc = all_hashes(text)

        print()

        for algo, value in sonuc.items():
            print(
                colored(algo, "green"),
                ":",
                value
            )

        input("\nDevam etmek için Enter...")

    elif secim == "2":

        path = input("\nDosya yolu: ")

        try:

            sonuc = all_file_hashes(path)

            print()

            for algo, value in sonuc.items():

                print(
                    colored(algo, "green"),
                    ":",
                    value
                )

        except Exception as e:

            error(str(e))

        input("\nEnter...")

    elif secim == "3":

        path = input("Dosya: ")
        algo = input(
            "Algoritma (sha256): "
        ) or "sha256"

        beklenen = input(
            "Hash: "
        )

        sonuc, veri = verify_hash(
            path,
            beklenen,
            algo
        )

        print()

        if sonuc:
            success("Hash doğrulandı.")
        else:
            error("Hash eşleşmedi.")

        print(veri)

        input("\nEnter...")

    elif secim == "4":

        file1 = input("1. Dosya: ")
        file2 = input("2. Dosya: ")

        result = compare_files(
            file1,
            file2,
            "sha256"
        )

        print()

        if result["success"]:

            if result["same"]:
                success("Dosyalar aynı.")
            else:
                warning("Dosyalar farklı.")

        else:

            error(
                result["message"]
            )

        input("\nEnter...")

    elif secim == "5":

        folder = input(
            "Klasör yolu: "
        )

        result = scan_folder(
            folder,
            "sha256"
        )

        print()

        if result["success"]:

            success(
                f"{result['total_files']} dosya bulundu."
            )

        else:

            error(
                result["message"]
            )

        input("\nEnter...")

    elif secim == "6":

        show_history()
        input("\nEnter...")

    elif secim == "7":

        show_logs()
        input("\nEnter...")

    elif secim == "8":

        settings_menu()

    elif secim == "0":

        success("Görüşürüz.")
        break

    else:

        error("Geçersiz seçim.")
        input("\nEnter...")
