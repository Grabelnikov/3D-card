#!/usr/bin/env python3
import http.server
import socketserver
import os

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == "__main__":
    PORT = 8000
    os.chdir('/Users/andreygrabelnikov/Development/3D card')
    
    with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        print("No-cache headers enabled for development")
        print("Press Ctrl+C to stop")
        httpd.serve_forever()