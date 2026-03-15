from http.server import BaseHTTPRequestHandler, HTTPServer
from roman import to_roman, to_arabic
from urllib.parse import parse_qs, urlparse

HTML = """
<html>
<head>
<title>Roman Converter</title>
</head>
<body>
<h2>Roman ↔ Arabic Converter</h2>

<form action="/convert">
<input name="value" placeholder="Enter number or roman">
<button type="submit">Convert</button>
</form>

<p>{result}</p>

</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/":
            self.respond("")

        elif parsed.path == "/convert":
            params = parse_qs(parsed.query)
            value = params.get("value", [""])[0]

            try:
                if value.isdigit():
                    result = f"{value} → {to_roman(int(value))}"
                else:
                    result = f"{value.upper()} → {to_arabic(value)}"

            except Exception as e:
                result = str(e)

            self.respond(result)

    def respond(self, result):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML.format(result=result).encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Open http://localhost:8000")
    server.serve_forever()
    