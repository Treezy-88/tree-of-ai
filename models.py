from database import get_db

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get_by_username(username):
        db = get_db()
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        if user is None:
            return None
        else:
            return User(user['id'], user['username'], user['password'])

    @staticmethod
    def create_new_user(username, password):
        db = get_db()
        db.execute(
            'INSERT INTO user (username, password) VALUES (?, ?)',
            (username, password)
        )
        db.commit()