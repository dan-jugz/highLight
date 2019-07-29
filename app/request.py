from app import app
import urllib.request,json
from .models import source

Source = source.Source

#Getting the api key
api_key=app.config['NEWS_API_KEY']

#Getting the news source base url
sources_base_url=app.config['NEWS_SOURCES_BASE_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url=sources_base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data=url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results=None

        if get_sources_response['sources']:
            sources_result_list=get_sources_response['sources']
            sources_results = process_results(sources_result_list)

    return sources_results        
