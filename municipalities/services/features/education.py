""" Характеристики зон ответственности сферы деятельности образование"""

from .abstract_class import Feature


class MunicipalityProvisionKindergartens(Feature):
    """ Обеспеченность детскими садами """

    @classmethod
    def indicator(cls) -> int:
        ...


if __name__ == '__main__':
    MunicipalityProvisionKindergartens.indicator()
