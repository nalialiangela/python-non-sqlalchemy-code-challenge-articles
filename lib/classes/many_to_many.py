class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        elif not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")
        elif hasattr(self, "_title"):
            raise AttributeError("Title cannot be reset")
        else:
            self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        self._magazine = magazine


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        elif len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        elif hasattr(self, "_name"):
            raise AttributeError("Name cannot be reset")
        else:
            self._name = name
    
    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({article.magazine.category for article in self.articles()}) or None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        elif not 2 <= len(name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        else:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string.")
        if len(value) == 0:
            raise ValueError("Category must have at least one character.")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return list([article.title for article in self.articles()]) or None

    def contributing_authors(self):
        authors_contributes  = {}
        for article in self.articles():
            author = article.author
            if author in authors_contributes:
                authors_contributes[author] += 1
            else:
                authors_contributes[author] = 1
        return [author for author, count in authors_contributes.items() if count > 2] or None
    
    @classmethod
    def top_publisher(cls):
        return (
            max(cls.all, key=lambda magazine: len(magazine.articles()))
            if Article.all
            else None
        )