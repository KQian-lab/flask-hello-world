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



@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgres://lab_10_db_vxl3_user:N0Pzj8hQDKtJ8iaruo6lUrtrdNtbuej9@dpg-co669gq1hbls73b5f0r0-a/lab_10_db_vxl3")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Create successful"

@app.route('/db_insert', methods=['POST'])
def db_insert():
    conn = psycopg2.connect("postgres://lab_10_db_vxl3_user:N0Pzj8hQDKtJ8iaruo6lUrtrdNtbuej9@dpg-co669gq1hbls73b5f0r0-a/lab_10_db_vxl3")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Basketball (First, Last, City, Name, Number) VALUES
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    """)
    conn.commit()
    conn.close()
    return ("Sucessfully inserted")


@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://lab_10_db_vxl3_user:N0Pzj8hQDKtJ8iaruo6lUrtrdNtbuej9@dpg-co669gq1hbls73b5f0r0-a/lab_10_db_vxl3")
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string += "<table>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"
    return response_string


@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://lab_10_db_vxl3_user:N0Pzj8hQDKtJ8iaruo6lUrtrdNtbuej9@dpg-co669gq1hbls73b5f0r0-a/lab_10_db_vxl3")
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"
