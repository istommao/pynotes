from wsgiref.simple_server import make_server

def wsgi_handler(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)

    return ['Hello wsgiref'.encode()]

httpd = make_server('', 7000, wsgi_handler)
print("Serving on port http://127.0.0.1:7000...")

httpd.serve_forever()

