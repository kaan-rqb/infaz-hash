# history.py

import os
import json
from datetime import datetime

HISTORY_DIR = "history"
HISTORY_FILE = os.path.join(
    HISTORY_DIR,
    "history.json"
)


def create_history():

    if not os.path.exists(HISTORY_DIR):
        os.makedirs(HISTORY_DIR)

    if not os.path.exists(HISTORY_FILE):

        with open(
            HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump([], f)


def load_history():

    create_history()

    try:

        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except:
        return []


def save_history(data):

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


def add_history(action, target, result):

    history = load_history()

    history.append({
        "time": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "action": action,
        "target": target,
        "result": result
    })

    save_history(history)


def show_history():

    history = load_history()

    print("\n=== GEÇMİŞ ===\n")

    if not history:
        print("Geçmiş boş.")
        return

    for i, item in enumerate(history, start=1):

        print("=" * 50)
        print(f"Kayıt #{i}")
        print(f"Tarih : {item['time']}")
        print(f"İşlem : {item['action']}")
        print(f"Hedef : {item['target']}")
        print(f"Sonuç : {item['result']}")
        print("=" * 50)


def search_history(keyword):

    history = load_history()

    results = []

    keyword = keyword.lower()

    for item in history:

        if (
            keyword in item["action"].lower()
            or keyword in item["target"].lower()
            or keyword in str(item["result"]).lower()
        ):
            results.append(item)

    return results


def print_search(keyword):

    results = search_history(keyword)

    print(f"\nArama: {keyword}\n")

    if not results:
        print("Sonuç bulunamadı.")
        return

    for item in results:

        print("=" * 50)
        print(f"Tarih : {item['time']}")
        print(f"İşlem : {item['action']}")
        print(f"Hedef : {item['target']}")
        print(f"Sonuç : {item['result']}")
        print("=" * 50)


def clear_history():

    save_history([])


if __name__ == "__main__":

    add_history(
        "TEXT_HASH",
        "Merhaba",
        "a1b2c3d4"
    )

    add_history(
        "FILE_HASH",
        "test.txt",
        "f4e3d2c1"
    )

    show_history()

    print_search("text")
