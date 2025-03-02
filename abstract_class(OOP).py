# from abc (abstract base class) import ABC (Abstract Base Class) and abstractmethod
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass

# now Stream (base or parent) class become abstract base class


class Stream(ABC):

    def __init__(self):
        self.opened = True

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

# read become and abstract method due to the abstractmethod decorator.
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):

    def read(self):
        return "Data is reading from file..."


class NetworStream(Stream):

    def read(self):
        return "Data is reading from network..."


# stream = Stream() # now it will give us an error.

file_stream = FileStream()
print(file_stream.read())
