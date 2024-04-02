import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Kevin Qian in 3308'






@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab_10_db_vxl3_user:N0Pzj8hQDKtJ8iaruo6lUrtrdNtbuej9@dpg-co669gq1hbls73b5f0r0-a/lab_10_db_vxl3")
    conn.close()
    return "Connection to DB successful"
