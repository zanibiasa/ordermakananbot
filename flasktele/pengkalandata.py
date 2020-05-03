from flasktele import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, unique=True, nullable=False)
    nama = db.Column(db.String(120), unique=False, nullable=True)

    makanan = db.relationship('Makanan', backref='kedai', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.nama}')"


class Makanan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namamakanan = db.Column(db.String(50), unique=False, nullable=True)
    harga = db.Column(db.Integer, nullable=True)
    kedai_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
