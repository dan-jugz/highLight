class Source:
    '''
    Source class that defines the News sources' objects
    '''
    def __init__(self,id,name,desc,url,category,language,country):
        self.id=id
        self.name=name
        self.desc=desc
        self.url=url
        self.category=category
        self.language=language
        self.country=country

class Article:
    '''
    Article class that defines the articles objects
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
        self.content=content