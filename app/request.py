from app import app
import urllib.request,json
from .models import source

Source = source.Source

#Getting the api key
api_key=app.config['NEWS_API_KEY']

#Getting the news source base url
sources_base_url=app.config['NEWS_SOURCES_BASE_URL'