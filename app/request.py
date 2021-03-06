from app import main
import urllib.request,json
from .models import News,Newsarticles

#News = models.News
#Newsarticles = models.Newsarticles

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
articles_url = None

def configure_request(app):
    global api_key, base_url, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]
    articles_url = app.config['ARTICLES_BASE_URL']



def process_newsresults(source_list):
    '''
    Function that process the source results and transforms them to a list objects
    Args:
        source_list: A list of dictionaries that contains source details
    Returns:
        source_results: A list of source objects
    '''

    source_results = []

    for sourced_item in source_list:
        id = sourced_item.get('id')
        name = sourced_item.get('name')
        description = sourced_item.get('description')
        title = sourced_item.get('title')
        category = sourced_item.get('category')
        url = sourced_item.get('url')
        country = sourced_item.get('country')


        if description:
             source_object = News(id,name, description, title, category,url,country)
             source_results.append(source_object)

    return source_results

def get_newssources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newssources_url = base_url.format(category, api_key)
    # print(get_newssources_url)

    with urllib.request.urlopen(get_newssources_url) as url:
        get_newssources_data = url.read()
        get_newssources_response = json.loads(get_newssources_data)

        sources_results = None

        if get_newssources_response['sources']:
            sources_results_list = get_newssources_response['sources']
            sources_results = process_newsresults(sources_results_list)

    return sources_results



def get_newspaperarticles(news_id):
    '''
    Function that gets articles based on the source id
    '''
    get_articlelocation_url = articles_url.format(news_id, api_key)

    print(get_articlelocation_url)

    with urllib.request.urlopen(get_articlelocation_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            search_articles_list = articles_location_response['articles']
            articles_location_results = process_newspaperarticles(search_articles_list)
    
        print(articles_location_results)

    return articles_location_results


def process_newspaperarticles(my_articles):
    '''
    Function that processes the json results for the articles
    '''
    article_location_list = []

    for article in my_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')

        if urlToImage:
            article_source_object = Newsarticles(author, title, description, url, urlToImage)
            article_location_list.append(article_source_object)

    print(article_location_list)
    return article_location_list
