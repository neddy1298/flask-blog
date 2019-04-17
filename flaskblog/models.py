from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, ma, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f(User('{self.username}', '{self.email}', '{self.image_file}'))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu = db.Column(db.String(20), unique=True, nullable=False)
    keterangan = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False)


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(20), unique=True, nullable=False)
    alamat = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')


class Kamar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(20), unique=True, nullable=False)
    harga = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    fasilitas = db.Column(db.String(60), nullable=False)
    stok = db.Column(db.Integer, nullable=False)

class UserSchema(ma.Schema):
    class Meta:
        fields=('id','username','email','image_file','password')

class PostSchema(ma.Schema):
    class Meta:
        fields=('id','title','date_posted','content','user_id')

class MenuSchema(ma.Schema):
    class Meta:
        fields=('id','menu','keterangan','image_file')

class HotelSchema(ma.Schema):
    class Meta:
        fields=('id','nama','alamat','image_file')

class KamarSchema(ma.Schema):
    class Meta:
        fields=('id','nama','harga','image_file','fasilitas','stok')