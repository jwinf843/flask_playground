from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {
        'username': 'jwinf843',
    }

    posts = [
        {
            'author': {'username': 'john360n'},
            'body': 'Rainy day in Osaka'
        },
        {
            'author': {'username': 'jwinf843'},
            'body': 'Watched Sorry to Bother You last night'
        },
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)