
## How to initialize database and use homework

 - `cd stream && python database.py`
 - `gunicorn -b 127.0.0.1:8000 stream.main:app`
 - Open [127.0.0.1:8000](127.0.0.1:8000) in your browser
