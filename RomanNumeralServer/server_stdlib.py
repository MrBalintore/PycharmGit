from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
from roman import to_roman, to_arabic


class Handler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        path = urlparse(self.path).path
        parts = path.strip("/").split("/")

        try:
            if parts[0] == "to_roman":
                number = int(parts[1])
                result = to_roman(number)
                self.send_json({"input": number, "roman": result})

            elif parts[0] == "to_arabic":
                roman = parts[1]
                result = to_arabic(roman)
                self.send_json({"input": roman, "arabic": result})

            else:
                self.send_json({"error": "Invalid endpoint"}, 404)

        except Exception as e:
            self.send_json({"error": str(e)}, 400)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Server running on http://localhost:8000")
    server.serve_forever()
    