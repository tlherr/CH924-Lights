from flask import Flask
import time


class HTTPServerManager:

    # Variables
    HTTP_HOST = "0.0.0.0"
    HTTP_PORT = 8000
    coin_machine = None
    app = Flask(import_name="CornerPocket")

    def __init__(self, coin_machine):
        self.coin_machine = coin_machine

    def start_server(self):
        # TODO: Disable debug = True in production environment to avoid remote arbitrary code execution
        self.app.run(host=self.HTTP_HOST, port=self.HTTP_PORT, debug=True, use_reloader=False)
        print time.asctime(), ">> HTTP Server Started - %s:%s <<" % (self.HTTP_HOST, self.HTTP_PORT)

    def stop_server(self):
        self.app.stop()
        print time.asctime(), ">> HTTP Server Stopped - %s:%s <<" % (self.HTTP_HOST, self.HTTP_PORT)

    @app.route('/')
    def hello_world(self):
        return 'Hello World!'
