from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', 'password'),
        database=os.environ.get('DB_NAME', 'myapp_db')
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT 1')
        result = cursor.fetchone()
        db_status = "Conectat la MySQL!"
        cursor.close()
        conn.close()
    except Exception as e:
        db_status = f"Eroare conectare MySQL: {str(e)}"
    
    return render_template('index.html', status=db_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)