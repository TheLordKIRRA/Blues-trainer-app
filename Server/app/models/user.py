from app.db.database import db
fromwerkzeug.security import generate_password_hash, check_password_hash #There is a missing space between from and werkzeug.security
class User(db.Model):                                                    #We should make a overall table to make it easier to call these from other files
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):                                    #There is no internal validation layers for this code which could serve as a necessary failsafe incase it is ever needed
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
