from flask import Flask
import time, logging
from AdminView import AdminView
from RESTView import RESTView


class HTTPServerManager:
    # Variables
    HTTP_HOST = "0.0.0.0"
    HTTP_PORT = 8000
    app = Flask(import_name="CornerPocket")

    def __init__(self, coin_machine, light_manager):
        print("Initializing HTTP Server Manager")
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        AdminView.coin_machine = coin_machine
        AdminView.light_manager = light_manager
        RESTView.coin_machine = coin_machine
        RESTView.light_manager = light_manager
        self.app.add_url_rule('/admin', view_func=AdminView.as_view('admin_view'), methods=['GET', 'POST', ])
        self.app.add_url_rule('/api', view_func=RESTView.as_view('rest_view'), methods=['GET', 'POST', ])

    def start_server(self):
        self.app.run(host=self.HTTP_HOST, port=self.HTTP_PORT, debug=False, use_reloader=False)
        print time.asctime(), ">> HTTP Server Started - %s:%s <<" % (self.HTTP_HOST, self.HTTP_PORT)

    def stop_server(self):
        self.app.stop()
        print time.asctime(), ">> HTTP Server Stopped - %s:%s <<" % (self.HTTP_HOST, self.HTTP_PORT)
