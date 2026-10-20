from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"Hello DevOps! Day 1 Complete!")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
    print("Server running on port 8080...")
    server.serve_forever()