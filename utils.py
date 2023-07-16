```python
import sqlite3
from flask import g

DATABASE_URI = 'sqlite:///mydatabase.db'

def connect_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_URI)
    return db

def query_db(query, args=(), one=False):
    cur = connect_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def format_response(data, status_code):
    return {
        'status': 'success' if status_code == 200 else 'error',
        'data': data
    }, status_code

def close_db():
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
```