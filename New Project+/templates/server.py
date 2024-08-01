#server.py


import sqlite3
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            username = data['username']
            password = hashlib.sha256(data['password'].encode()).hexdigest()

            conn = sqlite3.connect("userdata.db")
            cur = conn.cursor()

            cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
            
            if cur.fetchall():
                self._set_headers(200)
                self.wfile.write("Login Successful!".encode())
            else:
                self._set_headers(401)
                self.wfile.write("Login Failed!".encode())
            conn.close()
        else:
            self._set_headers(404)
            self.wfile.write("Not Found".encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=9999):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

