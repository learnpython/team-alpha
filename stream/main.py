

def app(environ, start_response):
    data = "test"
    start_response ('200 OK', [
        ('Content-Type', 'text/plain'),
        ('content-Length', str(len(data))),
    ])
    return iter([data])
 
