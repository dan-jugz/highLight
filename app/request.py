from app import app
import urllib.request,json
from .models import source

Source = source.Source

#Getting the api key
api_key=app.config['NEWS_API_KEY']

#Getting the news source base url
sources_base_url=app.config['NEWS_SOURCES_BASE_URL']

#Getting a news source articles
articles_base_url=app.config['NEW_ARTICLES_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url=sources_base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data=url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results=None

        if get_sources_response['sources']:
            sources_result_list=get_sources_response['sources']
            sources_results = process_results(sources_result_list)

    return sources_results  


def process_results(sources_list):
    '''
    Function that processes the source_result_list and transforms them to a list of objects
    Args:
        sources_list:A list of dictionaries that contain news sources 
     Returns:
        sources_results:A list of new source objects   
    '''

    sources_results=[]
    for source_item in sources_list:
        id=source_item.get('id')
        name=source_item.get('name')
        desc=source_item.get('description')
        url=source_item.get('url')
        category=source_item.get('category')
        language=source_item.get('language')
        country=source_item.get('country')

        source_obj=Source(id,name,desc,url,category,language,country)
        sources_results.append(source_obj)

   
    return sources_results 

def get_articles(id):
    '''
    Function that fetches a single news source and returns the source's articles
    '''

    get_articles_url=articles_base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data=url.read()
        get_articles_response=json.loads(get_articles_data)

        articles_results=None

        if get_articles_response['articles']:
            articles_result_list=get_articles_response['articles']
            articles_results=process_article_results(articles_result_list)

    return articles_results        
        
