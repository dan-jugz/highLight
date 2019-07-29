from flask import render_template
from app import app

# Views
@app.route('/')
@app.route('/newswatch')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'NEWS HIGHLIGHTS APP '
    return render_template('index.html',title = title)
    
    @app.route("/newswatch/<source_id>")
    
def news_source(source_id):
    '''
    View new_source page function that returns a news source page and its data
    '''
    return render_template('newsSource.html',id =source_id)