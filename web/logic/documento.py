
class Document(object):
    

    def __init__(self, id , title: str ,category,n_pages,author):
        
        
        self._id=id
        self._title = title
        self._category = category
        self._n_pages = n_pages
        self._author = author

        

    @property
    def id(self) -> int:
        
        return self._id

    @id.setter
    def id(self, id: int):
        
        self._id = id

    @property
    def title(self) -> str:
        
        return self._title

    @title.setter
    def title(self, title: str):
        
        self._title = title
    
    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, category: str):
        self._category = category

    @property
    def n_pages(self) ->int:
        return self._n_pages

    @n_pages.setter
    def n_pages(self, n_pages: int):
        self._n_pages = n_pages

    @property
    def author(self) ->str:
        return self._author

    @author.setter
    def author(self, author: str):
        self._author= author

    def __str__(self):
        """ Returns str of document.
          :returns: sting document
          :rtype: str
        """
        return '({0}, {1}, {2},{3},{4})'.format(self.id, self.title,self.category, self.n_pages, self.author)

   

        

if __name__ == '__main__':
    l=Document(id= 12154411, title= 'juegos del trono', category='literatura ', n_pages= 54, author='luis ruz' )
    l.title="juabnd"
    print(l)
    
        
        
    