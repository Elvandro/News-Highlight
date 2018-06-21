from app import app
import urllib.request, json
from .models import source
from .models import article

Source = source.Source
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the source url
source_url = app.config['NEWS_SOURCES_URL']
# Getting the article url
article_url = app.config['NEWS_ARTICLE_URL']


def get_news(category):
    '''
    Function that gets json response to our url request
    '''
    get_news_url = source_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(news_list):
    '''
    Function that processes source results and transfroms them to a list
    '''
    source_results = []
    for source in news_list:
         id = source.get('id')
         name = source.get('name')
         description = source.get('description')
         url = source.get('url')
         category = source.get('category')
         country = source.get('country')
         if url:
             source_object = Source(id,name,description,url,category,country)
             source_results.append(source_object)

    return source_results

def get_articles(id):
    '''
    Function that gets json response to our url request
    '''
    get_aticle_url = article_url.format(api_key)
    with urllib.request.urlopen(get_aticle_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(articles_list):
    '''
    A function that will process the dictionary and output a list of objects(article_results).
    '''
    article_results = []
    source_dictionary = {}
    for result in articles_list:
        source_id = result['source']
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        print(name)

        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        datePublished = result.get('datePublished')

        if url:
            print(id)
            source_object = Article(id, name, author,description, url, datePublished)
            article_results.append(source_object)

    return article_results        
