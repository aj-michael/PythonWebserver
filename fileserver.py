from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

PORT_NUMBER = 8002

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        f = open(curdir+sep+self.path)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(f.read())
        return

try:
    server = HTTPServer(('',PORT_NUMBER),Handler)
    print 'Started server on port ', PORT_NUMBER
    server.serve_forever()

except KeyboardInterrupt:
    print '\nserver shutting down'
    server.socket.close()
