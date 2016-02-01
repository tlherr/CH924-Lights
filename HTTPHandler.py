import BaseHTTPServer

class HTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    global pulses
    global cash
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body>")
        s.wfile.write("<p>Cash: {0}</p>".format(cash))
        s.wfile.write("<p>Pulses: {0}</p>".format(pulses))
        s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")