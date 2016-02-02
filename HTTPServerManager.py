import BaseHTTPServer
from flask import Flask
import time


class HTTPServerManager:

    # Variables
    HTTP_HOST = "0.0.0.0"
    HTTP_PORT = 8000
    app = None

    def __init__(self, coin_machine):
        self.app = Flask(__name__)

    def start_server(self):
        self.app.run(debug=False, use_reloader=False)
        print time.asctime(), ">> HTTP Server Started - %s:%s <<" % (self.HTTP_HOST, self.HTTP_PORT)

    def stop_server(self):
        self.app.stop()
        print time.asctime(), ">> HTTP Server Stopped - %s:%s <<" % (self.HTTP_HOST, self.HTTP_PORT)

    @app.route('/')
    def hello_world(self):
        return 'Hello World!'
