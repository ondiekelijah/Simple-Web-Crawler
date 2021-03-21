from app import db

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    results = db.Column(db.Text)

    def __repr__(self):
        return "<Data %r>" % self.url
