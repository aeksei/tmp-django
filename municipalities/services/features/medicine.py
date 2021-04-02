""" Характеристики зон ответственности сферы деятельности медицина"""

from .abstract_class import Feature


class MunicipalityAmbulanceAvailability(Feature):
    """ Обеспеченность скорой медицинской помощью """

    @classmethod
    def indicator(cls) -> int:
        ...


if __name__ == '__main__':
    MunicipalityAmbulanceAvailability.indicator()
