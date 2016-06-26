from abc import ABCMeta, abstractmethod


class AbstractRepository(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def save(self):
        pass
