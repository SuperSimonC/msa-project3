from app import db

# Models
class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(32))
    content = db.Column(db.Text)

    def __repr__(self):
        return '<Post %r>' % self.date