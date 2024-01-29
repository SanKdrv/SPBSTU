from typing import Union


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if type(new_name) is str:
            self._name = new_name
        else:
            raise ValueError("Error")

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        if type(new_author) is str:
            self._author = new_author
        else:
            raise ValueError("Error")


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if isinstance(new_pages, int) and new_pages > 0:
            self._pages = new_pages
        else:
            raise ValueError("Error")


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: Union[int, float]):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> Union[int, float]:
        return self._duration

    @duration.setter
    def duration(self, new_duration: Union[int, float]) -> None:
        if isinstance(new_duration, Union[int, float]) and new_duration > 0:
            self._duration = new_duration
        else:
            raise ValueError("Error")
