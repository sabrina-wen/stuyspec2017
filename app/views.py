from flask import render_template
from app import app, db, models
import datetime

@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'timestamp': '2017-04-15 09:41:03',
            'articleID': 106,
            'title': 'New York',
            'authors': [
                {'name': 'George Zheng'},
                {'name': 'Jason Kao'},
            ],
            'body': 'Beautiful day in New York!',
            'viewcount': 6,
            'tags': [3, 4, 2, 1, 5]
        },
        {
            'timestamp': '2017-04-15 09:49:03',
            'articleID': 109,
            'title': 'Stuyvesant!',
            'authors': [
                {'name': 'Sabrina Wen'},
                {'name': 'Angela Tom'},
            ],
            'body': 'Stuyvesant High School provides excellent education.',
            'viewcount': 10,
            'tags': [9, 10, 0, 34, 2]
        },
        {
            'timestamp': '2017-04-15 09:49:03',
            'articleID': 109,
            'title': 'Stuyvesant!',
            'authors': [
                {'name': 'Sabrina Wen'},
                {'name': 'Angela Tom'},
            ],
            'body': 'Stuyvesant High School provides excellent education.',
            'viewcount': 10,
            'tags': [9, 10, 0, 34, 2]
        },
        {
            'timestamp': '2017-04-15 09:49:03',
            'articleID': 109,
            'title': 'Stuyvesant!',
            'authors': [
                {'name': 'Sabrina Wen'},
                {'name': 'Angela Tom'},
            ],
            'body': 'Stuyvesant High School provides excellent education.',
            'viewcount': 10,
            'tags': [9, 10, 0, 34, 2]
        }
    ]
    return render_template("index.html",
                           title="Stuyvesant Spectator",
                           posts=posts)

def write_article(user, article):
    u = models.User(nickname='susan', email='susan@email.com')


def laod_articles():
    return 0

# for testing purposes
@app.route('/article-test')
def test_article():
    return render_template("article.html",
                           title="Article")
