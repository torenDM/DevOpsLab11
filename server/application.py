"""DevOps Lab 11: simple HTTP server for CI/CD demo."""

import http.server
import socketserver

PORT = 8000


class TestMe:
    """Small class used in unit tests."""

    def take_five(self) -> int:
        """Return constant 5."""
        return 5

    def port(self) -> int:
        """Return server port."""
        return PORT


def main() -> None:
    """Start a simple HTTP server on PORT."""
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
