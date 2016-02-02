import BaseHTTPServer


class HTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    coin_machine = None

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Title goes here.</title></head>")
        self.wfile.write("<body>")
        self.wfile.write("<p>Current Cash: {:0,.2f}</p>".format(self.coin_machine.money))
        self.wfile.write("</body></html>")