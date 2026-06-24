# 1. 
sudo dnf update -y
sudo reboot

# 2. vimのインストール
sudo dnf install vim -y

# 3. Dockerリポジトリの追加
sudo dnf install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# 4. Dockerのインストール
sudo dnf install -y docker-ce docker-ce-cli containerd.io

# 5. Dockerの起動と自動起動有効化
sudo systemctl start docker
sudo systemctl enable docker

# 6. ec2-userをdockerグループに追加
sudo usermod -aG docker ec2-user

# 7. ログアウトせずにグループ権限を現在のセッションに即時反映
newgrp docker

# 8. /var/www 配下に作業ディレクトリを作成
sudo mkdir -p /var/www/my-docker-web

# 9. 作成したディレクトリの所有者を ec2-user に変更
sudo chown -R ec2-user:ec2-user /var/www/my-docker-web

# 10. 作業ディレクトリに移動
cd /var/www/my-docker-web

# 11. 独自のWebページを作成
vim index.html

# 12. Dockerファイルの作成
vim Dockerfile

# 内容 alpine:RHEL系向けのminmumDockerImage
# FROM nginx:alpine
# COPY index.html /usr/share/nginx/html/index.html

# コンテナイメージのビルド
docker build -t my-custom-web .

# コンテナの起動（ポート80）
docker run -d -p 80:80 --name my-web-container my-custom-web


# 現在のコンテナを強制削除
docker rm -f my-web-container
# ポート8080で再起動
docker run -d -p 8080:80 --name my-web-container my-custom-web

