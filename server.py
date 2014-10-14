from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8002

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("Hi there")
        return

try:
    server = HTTPServer(('',PORT_NUMBER),Handler)
    print 'Started server on port ', PORT_NUMBER
    server.serve_forever()

except KeyboardInterrupt:
    print '\nserver shutting down'
    server.socket.close()
