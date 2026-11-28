"""อ่านค่าตั้งค่า (config) จาก environment variable ตามหลัก 12-factor app

โค้ดชุดเดียวกันใช้ได้ทุก environment (dev/staging/prod) แค่เปลี่ยนค่า env var
"""

import os
from dataclasses import dataclass

LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


@dataclass(frozen=True)
class Settings:
    base_url: str       # ส่วนหน้าของลิงก์สั้น เช่น https://sho.rt
    database_path: str  # ที่อยู่ไฟล์ SQLite
    log_level: str      # ระดับ log ขั้นต่ำที่จะพิมพ์ออกมา


def load_settings() -> Settings:
    """อ่านค่าจาก env var ถ้าไม่ได้ตั้งไว้จะใช้ค่าเริ่มต้นสำหรับเครื่องนักพัฒนา"""
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    if log_level not in LOG_LEVELS:
        raise ValueError(
            f"LOG_LEVEL ต้องเป็นหนึ่งใน {', '.join(LOG_LEVELS)} แต่ได้ '{log_level}'"
        )
    return Settings(
        base_url=os.getenv("BASE_URL", "http://localhost:8000").rstrip("/"),
        database_path=os.getenv("DATABASE_PATH", "links.db"),
        log_level=log_level,
    )
