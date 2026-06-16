# reports.py

import os
import json
from datetime import datetime


REPORT_DIR = "reports"


def create_report_folder():

    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)


def timestamp():

    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def save_txt_report(data, report_name=None):

    create_report_folder()

    if report_name is None:
        report_name = f"report_{timestamp()}.txt"

    report_path = os.path.join(
        REPORT_DIR,
        report_name
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write("=" * 60 + "\n")
        f.write("INFXZ HASH TOOL REPORT\n")
        f.write("=" * 60 + "\n\n")

        if isinstance(data, dict):

            for key, value in data.items():

                if isinstance(value, list):

                    f.write(f"{key}:\n")

                    for item in value:
                        f.write(
                            json.dumps(
                                item,
                                ensure_ascii=False,
                                indent=4
                            )
                        )
                        f.write("\n")

                else:
                    f.write(f"{key}: {value}\n")

        else:
            f.write(str(data))

    return report_path


def save_json_report(data, report_name=None):

    create_report_folder()

    if report_name is None:
        report_name = f"report_{timestamp()}.json"

    report_path = os.path.join(
        REPORT_DIR,
        report_name
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )

    return report_path


def load_json_report(report_path):

    if not os.path.isfile(report_path):
        return None

    with open(
        report_path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def list_reports():

    create_report_folder()

    reports = []

    for file in os.listdir(REPORT_DIR):

        full_path = os.path.join(
            REPORT_DIR,
            file
        )

        reports.append({
            "name": file,
            "path": full_path,
            "size": os.path.getsize(full_path)
        })

    return reports


def print_reports():

    reports = list_reports()

    print("\n=== RAPORLAR ===\n")

    if not reports:
        print("Rapor bulunamadı.")
        return

    for i, report in enumerate(reports, start=1):

        print(
            f"[{i}] {report['name']} "
            f"({report['size']} Byte)"
        )


if __name__ == "__main__":

    example_data = {
        "tool": "INFXZ Hash Tool",
        "algorithm": "SHA256",
        "hash": "abc123xyz",
        "status": "Success"
    }

    txt_path = save_txt_report(example_data)
    json_path = save_json_report(example_data)

    print("TXT Kaydedildi:")
    print(txt_path)

    print("\nJSON Kaydedildi:")
    print(json_path)

    print_reports()
