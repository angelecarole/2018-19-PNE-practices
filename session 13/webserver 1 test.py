import http.server
import socketserver

PORT = 8003


class TestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line :"+self.requestline)
        print("Cmd : +self.command")
        print("Path:"+self.path)
        content = "i am the happy server!"
        self.send_response(200)
        self.send_header('content-Type-', 'text/plain')
        self.send_header('content-Length-', len(str.encode(content)))

        self.wfile.write(str.encode(content))
        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    httpd.serve_forever()
