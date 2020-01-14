from abc import abstractmethod, ABC


class Middleware(ABC):

    @abstractmethod
    def get_name(self):
        return 'middleware'

    @abstractmethod
    def input(self, zencode, data, keys):
        pass

    @abstractmethod
    def output(self, zencode, data, keys):
        pass
