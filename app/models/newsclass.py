class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,title,description,category,url,country):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.category = category
        self.url = url
        self.country = country



class Newsarticles:
    '''
    Article class that defines the article objects
    '''

    def __init__(self, author, title, description, url, urlToImage):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
