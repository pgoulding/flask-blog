from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
  user = {'username': 'Bob'}
  print("index")
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

@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

