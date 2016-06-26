from abc import ABCMeta, abstractmethod


class InjectorInterface:

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_manager(self):
        pass
