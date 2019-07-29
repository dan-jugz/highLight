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