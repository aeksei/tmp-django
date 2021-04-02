from abc import ABC, abstractmethod


class Feature(ABC):
    """ Характеристика зоны ответственности муниципального округа или района"""
    @classmethod
    @abstractmethod
    def indicator(cls) -> int:
        """ Индикатор характеристики зоны ответственности """
        ...
