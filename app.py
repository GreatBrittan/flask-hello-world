import psycopg2
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect('postgres://lab10webserivce_db_user:SsT2IplvuawEg78StJeXKuI3VFBwrs9B@dpg-cl5al8a8vr0c73ajrrqg-a/lab10webserivce_db')
    conn.close()
    return "Database Connection Successful"