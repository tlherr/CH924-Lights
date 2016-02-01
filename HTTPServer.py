import BaseHTTPServer
import HTTPHandler
import signal

class HTTPServer:

    HTTP_HOST = "127.0.0.1"
    HTTP_PORT = 8000
    server = None

    def __init__(self):
        print("Initilizing new HTTP Server running on host: {0} port: {1}".format(self.HTTP_HOST, self.HTTP_PORT))
        self.server = BaseHTTPServer.HTTPServer((self.HTTP_HOST, self.HTTP_PORT), HTTPHandler)
        signal.signal(signal.SIGINT, self.signal_handler)	# SIGINT = interrupt by CTRL-C

    def start_server(self):
        # Setup stuff here...
        print("Server running")
        self.server.serve_forever()

    def signal_handler(self, signal, frame):
        print('You pressed Ctrl+C, exiting')
        self.server.server_close()