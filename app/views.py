from flask import render_template
from app import app
from .request import get_sources,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting the news sources
    business_sources=get_sources('business')
    entertainment_sources=get_sources('entertainment')
    general_sources=get_sources('general')
    health_sources=get_sources('health')
    science_sources=get_sources('science')
    sports_sources=get_sources('sports')
    tech_sources=get_sources('technology')
    
    title = 'Articles highLights APP '
    return render_template('index.html', title=title, business=business_sources,
                           entertainment=entertainment_sources, general=general_sources, health=health_sources,
                           science=science_sources, sports=sports_sources, tech=tech_sources)
    

@app.route("/newswatch/<source_id>")
def news_source(source_id):
    '''
    View new_source page function that returns a news source page and its data
    '''
    
    title=f"{source_id}-page"
    articles = get_articles(source_id)
    majorArticle= articles[0]
    major2article=articles[1:4]
    print(articles)
    return render_template('newsSource.html', title=title,articles=articles,majorArticle=majorArticle,major2article=major2article)
