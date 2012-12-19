import datetime

def app(environ, start_response):
    data = "time: {}, utctime: {}".format(
    	datetime.datetime.now().strftime("%H : %M"),
    	datetime.datetime.utcnow().strftime("%H : %M")
    )
    start_response ('200 OK', [
        ('Content-Type', 'text/plain'),
        ('content-Length', str(len(data))),
    ])
    return iter([data])
 
