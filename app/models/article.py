class Article:
    '''
    A class that defines our articles object
    '''

    def __init__(self, id ,name, title, author, description, url, datePublished):
        self.id = id
        self.name = name
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.datePublished = datePublished
