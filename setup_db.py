from app import app, db
from app.models import Article

db.drop_all()
db.create_all()

dates = [
    '01.01',
    '02.01',
    '03.01'
]

for date in dates:
    new_article = Article(date=date, content='Content')
    db.session.add(new_article)
db.session.commit()