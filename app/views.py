from flask import render_template
from app import app
from .request import get_newssources, get_newspaperarticles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    business_news = get_newssources('business')
    entertainment_news = get_newssources('entertainment')
    sports_news = get_newssources('sports')
    technology_news = get_newssources('technology')
    science_news = get_newssources('science')
    health_news = get_newssources('health')

    title = 'Home - Welcome to The best NEWS HIGHLIGHT Website online'
    return render_template('index.html', title = title, Business=business_news,Entertainment=entertainment_news, Sports=sports_news, Technology=technology_news,Science=science_news, Health=health_news)

@app.route('/newsatnine/<int:movie_id>')
def allthenews(news_id):
    '''
    A view news page function that returns the news details page and its data
    '''
    return render_template('newsatnine.html',id = news_id)