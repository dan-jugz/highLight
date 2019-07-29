class Article:
    '''
    Article class that defines the articles objects
    '''

    def __init__(self,author,title,desc,url,urlToImage,publishedAt,content):
        self.author=author
        self.title=title
        self.desc=desc
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
        self.content=content