from app import app
import urllib.request, json
from .models import movie

# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the source url
source_url = app.config['NEWS_SOURCES_BASE_URL']
# Getting the article url
article_url = app.config['NEWS_ARTICLE_BASE_URL']


def get_news():
    '''
    Function that gets json response to our url request
    '''
    get_news_url = source_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['results']:
            source_results_list = get_source_response['results']
            source_results = process_results(source_results_list)

    return source_results        
