แยกชั้น `api` / `service` / `repository` · config จาก env var · log JSON ออก stdout
| ตัวแปร | ค่าเริ่มต้น | ความหมาย |
|---|---|---|
| `BASE_URL` | `http://localhost:8000` | ส่วนหน้าของลิงก์สั้นที่ตอบกลับ |
| `DATABASE_PATH` | `links.db` | ที่อยู่ไฟล์ SQLite |
| `LOG_LEVEL` | `INFO` | ระดับ log ขั้นต่ำ (`DEBUG`, `INFO`, `WARNING`, `ERROR`) |
