from app import app
import urllib.request,json
from .models import newsclass

News = newsclass.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_newssources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newssources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_newssources_url) as url:
        get_newssources_data = url.read()
        get_sources_response = json.loads(get_newssources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_newsresults(sources_results_list)

    return sources_results

def process_newsresults(source_list):
    '''
    Function that process the source results and transforms them to a list objects
    Args:
        source_list: A list of dictionaries that contains source details
    Returns:
        source_results: A list of source objects
    '''

    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        title = source_item.get('title')
        category = source_item.get('category')
        url = source_item.get('url')


        if url:
             source_object = News(id,name, description, title, category,url)
             source_results.append(source_object)

    return source_results