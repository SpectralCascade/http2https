#!/usr/bin/python2

import string
import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Parse the URL and convert to https
            self.send_response(301)
            dest = "https://" + self.headers.get('Host') + self.path
            print("Redirecting to " + dest)
            self.send_header("Location", dest)
        finally:
            self.end_headers()
            self.finish()

if __name__ == '__main__':
    # Defaults to port 8080, but you can pass in a port instead if you wish.
    server_address = ('0.0.0.0', 8080 if len(sys.argv) < 2 else int(sys.argv[1]))
    httpd = HTTPServer(server_address, ProxyHTTPRequestHandler)
    print("HTTP to HTTPS redirect service is running.")
    httpd.serve_forever()

