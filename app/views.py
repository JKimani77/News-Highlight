from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best NEWS HIGHLIGHT Website online'
    return render_template('index.html', title = title)

@app.route('/newsatnine/<int:movie_id>')
def allthenews(news_id):

    '''
    A view news page function that returns the news details page and its data
    '''
    return render_template('newsatnine.html',id = news_id)