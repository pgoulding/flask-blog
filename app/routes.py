from flask import render_template
from app import app

@app.route('/')
@app.route('/index')


def index():
  user = {'username': 'Bob'}
  posts = [
    {
      'author' : {'username': 'Patrick'},
      'body' : 'Beautiful Day in Denver!'
    },
    {
      'author': {'username': 'Steve'},
      'body': 'How about them Eagles?'
    }
  ]

  return render_template('index.html', title='home', user=user, posts=posts)