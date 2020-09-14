from flask import render_template, request, redirect, url_for, jsonify
from app import app, models, db

Article = models.Article
title = 'My daily diary'

@app.route('/')
def home():
    articles = Article.query.all()
    articles.reverse()
    return render_template("home.html", title=title, articles=articles)


@app.route('/diary/', methods=['POST'])
def add_item():
    date = request.form.get('Date')
    Content = request.form.get('Content')
    
    new_article = Article(date=date, content=Content)
    
    # Add and commit the changes to the database
    db.session.add(new_article)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/diary/<int:id>', methods=['DELETE'])
def delete_article(id):
    article = Article.query.filter_by(id=id).first()
    
    if (article != None):
        msg = {
            'message': 'Delete successful'
        }
        db.session.delete(article)
        db.session.commit()
        return jsonify(msg), 200
	
    msg = {
        'message': 'not found'
    }
    return jsonify(msg), 204

@app.route('/AboutMe/')
def aboutMe():
    return render_template("aboutMe.html")
