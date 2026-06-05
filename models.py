from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class Sushi(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(1000010000),nullable=False)
    description=db.Column(db.String(20002000),nullable=True)

    image=db.Column(db.String(20002000),nullable=True)
class Main(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000010000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(20002000), nullable=True)

class Dop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000010000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(20002000), nullable=True)



class Main22(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000010000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(20002000), nullable=True)


class Main222(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000010000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(20002000), nullable=True)
