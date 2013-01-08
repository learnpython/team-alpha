import datetime
import sqlite3
import os

PWD = os.path.dirname(__file__)
conn = sqlite3.connect(os.path.join(PWD, 'stream.db'))

def app(environ, start_response):
    c = conn.cursor()
    rows = list(c.execute('SELECT * FROM photos ORDER BY description'))
    message = ""

    if not rows:
        message = "no photos"
    else:
        for photo in rows:
            message += '<img src="{}" alt="{}">\n'.format(photo[1], photo[2])

    data = "time: {}, utctime: {}<br>\n{}".format(
        datetime.datetime.now().strftime("%H : %M"),
        datetime.datetime.utcnow().strftime("%H : %M"),
        message
    )
    start_response ('200 OK', [
        ('Content-Type', 'text/html'),
        ('content-Length', str(len(data))),
    ])
    return iter([data])
 
