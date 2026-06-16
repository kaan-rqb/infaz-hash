# settings.py

import os
import json

CONFIG_DIR = "config"
SETTINGS_FILE = os.path.join(
    CONFIG_DIR,
    "settings.json"
)

DEFAULT_SETTINGS = {
    "theme": "red",
    "default_algorithm": "sha256",
    "auto_save_reports": True,
    "auto_save_history": True,
    "show_banner": True,
    "show_logs_on_error": True,
    "report_format": "json"
}


def create_config():

    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    if not os.path.exists(SETTINGS_FILE):

        with open(
            SETTINGS_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                DEFAULT_SETTINGS,
                f,
                indent=4
            )


def load_settings():

    create_config()

    try:

        with open(
            SETTINGS_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except:
        return DEFAULT_SETTINGS.copy()


def save_settings(settings):

    with open(
        SETTINGS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            settings,
            f,
            indent=4
        )


def get_setting(key):

    settings = load_settings()

    return settings.get(key)


def set_setting(key, value):

    settings = load_settings()

    settings[key] = value

    save_settings(settings)


def reset_settings():

    save_settings(
        DEFAULT_SETTINGS.copy()
    )


def show_settings():

    settings = load_settings()

    print("\n=== AYARLAR ===\n")

    for key, value in settings.items():

        print(
            f"{key}: {value}"
        )


def settings_menu():

    while True:

        print("""
=========================
      AYARLAR
=========================
1 - Ayarları Göster
2 - Tema Değiştir
3 - Varsayılan Algoritma
4 - Rapor Formatı
5 - Sıfırla
0 - Geri Dön
=========================
""")

        choice = input(
            "Seçim: "
        ).strip()

        if choice == "1":

            show_settings()

        elif choice == "2":

            theme = input(
                "Tema: "
            )

            set_setting(
                "theme",
                theme
            )

            print(
                "Tema güncellendi."
            )

        elif choice == "3":

            algo = input(
                "Algoritma: "
            )

            set_setting(
                "default_algorithm",
                algo
            )

            print(
                "Algoritma güncellendi."
            )

        elif choice == "4":

            fmt = input(
                "json/txt: "
            )

            set_setting(
                "report_format",
                fmt
            )

            print(
                "Format güncellendi."
            )

        elif choice == "5":

            reset_settings()

            print(
                "Ayarlar sıfırlandı."
            )

        elif choice == "0":

            break

        else:

            print(
                "Geçersiz seçim."
            )


if __name__ == "__main__":

    settings_menu()
