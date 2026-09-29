import unittest

from app.app import response_for_path


class ResponseTests(unittest.TestCase):
    def test_health_check_returns_ok(self):
        status, content_type, body = response_for_path("/health", 0)
        self.assertEqual(status, 200)
        self.assertEqual(content_type, "application/json")
        self.assertIn(b'"status": "ok"', body)

    def test_metrics_exposes_request_counter(self):
        status, content_type, body = response_for_path("/metrics", 7)
        self.assertEqual(status, 200)
        self.assertIn("text/plain", content_type)
        self.assertIn(b"task_board_http_requests_total 7", body)

    def test_unknown_path_returns_not_found(self):
        status, content_type, body = response_for_path("/missing", 0)
        self.assertEqual(status, 404)
        self.assertEqual(content_type, "application/json")
        self.assertIn(b"not found", body)


if __name__ == "__main__":
    unittest.main()
