"""repository ที่เก็บข้อมูลในไฟล์ SQLite"""

import sqlite3

from app.repository.base import Link, LinkRepository


class SQLiteLinkRepository(LinkRepository):
    def __init__(self, path: str):
        self.path = path
        with self._connect() as conn:
            conn.execute(
                """CREATE TABLE IF NOT EXISTS links (
                       code TEXT PRIMARY KEY,
                       url TEXT NOT NULL,
                       clicks INTEGER NOT NULL DEFAULT 0,
                       created_at TEXT NOT NULL
                   )"""
            )

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row  # ให้อ่านคอลัมน์ด้วยชื่อได้ เช่น row["url"]
        return conn

    def add(self, link: Link) -> None:
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO links (code, url, clicks, created_at) VALUES (?, ?, ?, ?)",
                (link.code, link.url, link.clicks, link.created_at),
            )

    def get(self, code: str) -> Link | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT code, url, clicks, created_at FROM links WHERE code = ?",
                (code,),
            ).fetchone()
        if row is None:
            return None
        return Link(row["code"], row["url"], row["clicks"], row["created_at"])

    def increment_clicks(self, code: str) -> None:
        with self._connect() as conn:
            conn.execute(
                "UPDATE links SET clicks = clicks + 1 WHERE code = ?",
                (code,),
            )

    def ping(self) -> None:
        with self._connect() as conn:
            conn.execute("SELECT 1 FROM links LIMIT 1")
