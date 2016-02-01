import BaseHTTPServer
import HTTPHandler
import signal

class HTTPServer:

    HTTP_HOST = "localhost"
    HTTP_PORT = 8000
    server = None

    def __init__(self):
        print("Initilizing new HTTP Server running on host: %s port: %s".format(self.HTTP_HOST, self.HTTP_PORT))
        self.server = BaseHTTPServer.HTTPServer((self.HTTP_HOST, self.HTTP_PORT), HTTPHandler)
        signal.signal(signal.SIGINT, self.signal_handler)	# SIGINT = interrupt by CTRL-C

    def start_server(self):
        # Setup stuff here...
        self.server.serve_forever()

    def signal_handler(self, signal, frame):
        print('You pressed Ctrl+C, exiting')
        self.server.server_close()