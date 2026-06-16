# logs.py

import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(
    LOG_DIR,
    "infxz.log"
)


def create_log_folder():

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if not os.path.exists(LOG_FILE):

        with open(
            LOG_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            f.write("=== INFXZ LOG SYSTEM ===\n")


def get_time():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def write_log(level, message):

    create_log_folder()

    log_line = (
        f"[{get_time()}] "
        f"[{level}] "
        f"{message}\n"
    )

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(log_line)


def info(message):

    write_log(
        "INFO",
        message
    )


def warning(message):

    write_log(
        "WARNING",
        message
    )


def error(message):

    write_log(
        "ERROR",
        message
    )


def success(message):

    write_log(
        "SUCCESS",
        message
    )


def read_logs():

    create_log_folder()

    with open(
        LOG_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


def show_logs():

    print("\n=== LOG KAYITLARI ===\n")

    print(read_logs())


def clear_logs():

    create_log_folder()

    with open(
        LOG_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "=== INFXZ LOG SYSTEM ===\n"
        )


def log_exception(exception):

    error(
        f"EXCEPTION -> {str(exception)}"
    )


if __name__ == "__main__":

    info("Program başlatıldı.")

    success(
        "Hash işlemi tamamlandı."
    )

    warning(
        "Dosya bulunamadı."
    )

    error(
        "Hash doğrulama başarısız."
    )

    show_logs()
