class Config:

    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_HEADLINES_BASE_URL='https://newsapi.org/v2/top-headlines?sources{}&apiKey={}'
    NEW_ARTICLES_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}