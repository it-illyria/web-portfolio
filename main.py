from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

PORT = 8000

about_me = "I am a full-stack software developer with over 3 years of experience and passion for creating web applications and learning new technologies."

projects = [
    {
        'name': 'it-illyria-ui',
        'description': 'A library component created for Angular.',
        'link': 'it_illyria_ui.html'
    },
    {
        'name': 'story-forge',
        'description': 'A story quiz game platform.',
        'link': 'story_forge.html'
    }
]

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/about':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'about_me': about_me}).encode('utf-8'))
        elif self.path == '/api/projects':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'projects': projects}).encode('utf-8'))
        else:
            super().do_GET()

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {PORT}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
