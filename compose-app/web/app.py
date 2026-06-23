from flask import Flask, request
import psycopg2
import os

app = Flask(__name__)

# /にアクセスされたときにこの関数が動く
@app.route('/')
def index():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'mydatabase'),
        user=os.environ.get('DB_USER', 'myuser'),
        password=os.environ.get('DB_PASSWORD', 'mypassword')
    )

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    html = """
    <h2>ユーザー一覧</h2>

    <form method="POST" action="/add">
        <input name="name" placeholder="名前を入力">
        <button type="submit">追加</button>
    </form>

    <ul>
    """

    
    for u in users:
        html += f"<li>ID:{u[0]} - 名前:{u[1]}</li>"

    html += "</ul>"
    return html



@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    if name == "":
        return "名前を入力してください。<a href='/'>戻る</a>"

    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'mydatabase'),
        user=os.environ.get('DB_USER', 'myuser'),
        password=os.environ.get('DB_PASSWORD', 'mypassword')
    )

    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()

    cursor.close()
    conn.close()

    return "追加しました。<a href='/'>戻る</a>"