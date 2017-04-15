from flask import Flask
import json, sys, calendar, datetime, psycopg2

app = Flask(__name__)

def default(obj):
    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
    millis = int(
        calendar.timegm(obj.timetuple()) * 1000 +
        obj.microsecond / 1000
    )
    return millis

#load the index file on startup
@app.route('/')
def root():
    return app.send_static_file('index.html')

#load the css file
@app.route('/style.css')
def css():
    return app.send_static_file('style.css')

#load the js file
@app.route('/script.js')
def js():
    return app.send_static_file('script.js')

#function to load a dropdown menu. grabs data and returns to js
@app.route("/popsites/")
def popsites():
  foo = []
  try:
    conn =  psycopg2.connect(host='myHost', user='myUserName', password='myPass', database='myDB')
    curs = conn.cursor()

    curs.execute('select site, sloc from sitelist order by site;')

    for row in curs:
      foo.append(row)

    return json.dumps(foo, default=default)
    
  except Exception as e:
    return str(e)
  finally:
	conn.close()

#function to insert data from a user form to a db
@app.route('/<mode>/<usite>/<uname>/<lat>/<lng>/')
def insertData(mode,usite,uname,lat,lng):
  foo = []
  try:
    conn =  psycopg2.connect(host='myHost', user='myUserName', password='myPass', database='myDB')
    curs = conn.cursor()

    curs.execute('INSERT INTO countdata (cdate, userid, site, '+mode+', ulat, ulong) VALUES (now(), \''+uname+'\', '+usite+', 1, '+lat+', '+lng+');')

    for row in curs:
      foo.append(row[0])

    return json.dumps(foo, default=default)
    
  except Exception as e:
    return str(e)
  finally:
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)

  