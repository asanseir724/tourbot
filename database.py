
# database.py
import psycopg2
from config import DATABASE_CONFIG

def get_db_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn
