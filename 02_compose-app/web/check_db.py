import psycopg2
import os
import sys

def check_connection():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'db'),
            database=os.environ.get('DB_NAME', 'mydatabase'),
            user=os.environ.get('DB_USER', 'myuser'),
            password=os.environ.get('DB_PASSWORD', 'mypassword'),
            connect_timeout=3
        )
        conn.close()
        sys.exit(0)
    
    except Exception:
        sys.exit(1)

if __name__ == '__main__':
    check_connection()
