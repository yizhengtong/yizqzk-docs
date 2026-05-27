#!/usr/bin/env python3
"""
天赋推送接收服务 — 接收文档站表单 POST，写入 _inbox/ 文件夹。
启动: python scripts/talent_server.py
端口: 8765
"""
import json
import os
import re
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

INBOX = Path("D:/ZM/yizgzq/_talent-inbox")
PORT = 8765


class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        if self.path != "/push":
            self.send_response(404)
            self._cors()
            self.end_headers()
            return

        try:
            length = int(self.headers.get("Content-Length", 0))
        except (ValueError, TypeError):
            self._reply(400, {"error": "invalid Content-Length"})
            return
        body = self.rfile.read(length).decode("utf-8")
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._reply(400, {"error": "invalid json"})
            return

        name = (data.get("name") or "untitled").strip()
        if not name:
            self._reply(400, {"error": "name required"})
            return

        filename = re.sub(r"[^a-zA-Z0-9_一-鿿]+", "_", name)
        filepath = INBOX / f"{filename}.json"
        INBOX.mkdir(parents=True, exist_ok=True)

        filepath.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[SAVED] {filepath}")
        self._reply(200, {"ok": True, "file": str(filepath)})

    def _reply(self, code, data):
        self.send_response(code)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]}")


if __name__ == "__main__":
    print(f"天赋推送服务启动: http://localhost:{PORT}/push")
    print(f"收件箱: {INBOX}")
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
