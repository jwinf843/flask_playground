from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {
        'username': 'jwinf843',
    }

    return render_template('index.html', title='Home', user=user)

app.run(debug=True)