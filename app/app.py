from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import logging
import os
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
REQUEST_COUNT = 0


def response_for_path(path, request_count):
    if path == "/":
        return 200, "text/html; charset=utf-8", (APP_DIR / "index.html").read_bytes()
    if path == "/health":
        return 200, "application/json", json.dumps({"status": "ok"}).encode("utf-8")
    if path == "/metrics":
        metrics = (
            "# HELP task_board_http_requests_total Total HTTP requests handled.\n"
            "# TYPE task_board_http_requests_total counter\n"
            f"task_board_http_requests_total {request_count}\n"
        )
        return 200, "text/plain; version=0.0.4; charset=utf-8", metrics.encode("utf-8")
    return 404, "application/json", json.dumps({"error": "not found"}).encode("utf-8")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global REQUEST_COUNT
        REQUEST_COUNT += 1
        status, content_type, body = response_for_path(self.path, REQUEST_COUNT)
        logging.info("http_request method=GET path=%s status=%s", self.path, status)
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string, *args):
        logging.info(format_string, *args)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    port = int(os.environ.get("PORT", "8080"))
    logging.info("starting team task board on port=%s", port)
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
