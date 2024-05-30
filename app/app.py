from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST", "mysql")
db_user = os.getenv("DB_USER", "root")
db_password = os.getenv("DB_PASSWORD", "password")
db_name = os.getenv("DB_NAME", "mydatabase")

def get_db_connection():
    """Establishes a connection to the MySQL database."""
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        database = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return jsonify(message=f"Connected to database: {database}")
    except mysql.connector.Error as err:
        return jsonify(error=str(err)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
