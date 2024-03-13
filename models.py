import shelve
from datetime import datetime
class Book_Datastore:

  # constructor
  def __init__(self):
    self.__datastore = shelve.open("data/book.db")

  # destructor 
  def __del__(self):
    self.__datastore.close()

  def add_instance(self, Book):
    self.__datastore[Book.get_hash()] = Book  

  def delete_instance(self, hash):
    del self.__datastore[hash]

  def get_books(self):
    return self.__datastore


class Book:
  def __init__(self, name, url):
    self.__name = name
    self.__url = url

    current_dateTime = datetime.now()
    hash_value = str(abs(hash(name + str(current_dateTime))))
    self.__hash = hash_value

  def get_name(self):
    return self.__name

  def get_url(self):
    return self.__url

  def get_hash(self):
    return self.__hash