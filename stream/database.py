import sqlite3

conn = sqlite3.connect('stream.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS "photos" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "url" TEXT UNIQUE,
        "description" TEXT);
''')

count = c.execute('SELECT count(id) FROM photos').fetchone()[0]

# c.execute('SELECT * FROM photos')
if count != 0:
    print "Rows count: {}".format(count)
else: 
    print "No data. Adding..."
    photos = [
        (None, "https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-prn1/75385_10151418995367994_918179528_n.jpg", "photo1"),
        (None, "https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-ash4/423258_10151412145917994_240960820_n.jpg", "photo2"),
        (None, "https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-prn1/553078_10151408586417994_877617997_n.jpg", "photo3"),
        (None, "https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-ash4/399982_10151403365027994_1664006880_n.jpg", "photo4"),
        (None, "https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-snc7/386768_10151401770542994_1117318597_n.jpg", "photo5"),
        (None, "https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash4/184453_10151399968232994_444719738_n.jpg", "photo6"),
        (None, "https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-prn1/154726_10151393676692994_1612893207_n.jpg", "photo7"),
        (None, "https://fbcdn-sphotos-d-a.akamaihd.net/hphotos-ak-ash3/547604_10151393108372994_2092660989_n.jpg", "photo8"),
        (None, "https://fbcdn-sphotos-e-a.akamaihd.net/hphotos-ak-ash3/576439_10151391483212994_38998924_n.jpg", "photo9"),
        (None, "https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-snc6/281635_10151390261202994_2007225954_n.jpg", "photo10"),
    ]
    c.executemany('INSERT INTO "photos" VALUES (?, ?, ?)', photos)
    conn.commit()
    print "Data added."
