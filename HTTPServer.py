import BaseHTTPServer
from HTTPHandler import HTTPHandler
import signal
import time

class HTTPServer:

    HTTP_HOST = "127.0.0.1"
    HTTP_PORT = 8000
    server = None

    def __init__(self):
        print("Initilizing new HTTP Server running on host: {0} port: {1}".format(self.HTTP_HOST, self.HTTP_PORT))
        self.server = BaseHTTPServer.HTTPServer((self.HTTP_HOST, self.HTTP_PORT), HTTPHandler)

    def start_server(self):
        print time.asctime(), "HTTP Server Started - %s:%s" % (self.HTTP_HOST, self.HTTP_PORT)
        self.server.serve_forever()
        try:
           self.server.serve_forever()
        except KeyboardInterrupt:
           pass
        self.server.server_close()
        print time.asctime(), "HTTP Server Stopped - %s:%s" % (self.HTTP_HOST, self.HTTP_PORT)