# alpineだと動かんかった
FROM python:3.10-slim

# mkdir /app cd /app
WORKDIR /app

# cp requirements.txt ./requirements.txt
COPY requirements.txt .

# リストをもとにライブラリのインストール
# --no-cache-dir:無駄なファイルを残さない
RUN pip install --no-cache-dir -r requirements.txt

# linux .(we/) を コンテナの. にコピー
COPY . .
RUN chmod +x entrypoint.sh

# 80ポートで通信しろ
EXPOSE 80

# コンテナ起動時に実行するファイル
ENTRYPOINT ["./entrypoint.sh"]

