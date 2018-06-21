from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():
    '''
    Function that returns the index page and its data
    '''

    general_list = get_news('general')
    health_list = get_news('health')
    business_list = get_news('business')
    technology_list = get_news('technology')
    sports_list = get_news('sports')
    entertainment_list = get_news('entertainment')

    return render_template('index.html',
                            general=general_list,
                            health=health_list,
                            business=business_list,
                            technology=technology_list,
                            sports=sports_list,
                            entertainment=entertainment_list)
