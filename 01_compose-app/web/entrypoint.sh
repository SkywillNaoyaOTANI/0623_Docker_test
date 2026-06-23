#!/bin/sh

echo "データベースの接続を確認しています..."

# dbにつながるか
python check_db.py

if [ $? -eq 0 ]; then
    echo "接続成功。Webアプリケーションを起動します。"
    
    # 1. .sh から gunicorn に切り替え
    # 2. 0.0.0.0(全てのIP)から80 portで受ける
    # 3. app.py : app = Flask(__name__)
    exec gunicorn --bind 0.0.0.0:80 app:app
else
    echo "DBに接続できません。メンテナンスページを表示します。"
    
    cd maintenance

    # 1. .sh から python に切り替え
    # 2. Python内蔵の http.server モジュールを起動し 80 で受ける
    exec python -m http.server 80
fi
