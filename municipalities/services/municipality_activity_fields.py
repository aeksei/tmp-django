from abc import ABC, abstractmethod

from municipalities.services.features import medicine, education


class ActivityFieldFeatures(ABC):
    """ Абстрактный класс для подсчета интегрального показателя сферы деятельности муниципального округа или района """

    @property
    @abstractmethod
    def integral_indicator(self) -> int:
        """ Свойство, возвращающиее интегральный показатель сферы деятельности """
        ...


class MunicipalityMedicine(ActivityFieldFeatures):
    """ Интегральный показатель сферы деятельности "Медицина" """

    def integral_indicator(self) -> int:
        features = [
            medicine.MunicipalityAmbulanceAvailability,
        ]

        return sum(feature.indicator() for feature in features)  # ToDo посчитать и вернуть интегральный показатель


class MunicipalityEducation(ActivityFieldFeatures):
    """ Интегральный показатель сферы деятельности "Образование" """

    def integral_indicator(self) -> int:
        features = [
            education.MunicipalityProvisionKindergartens,
        ]
        return sum(feature.indicator() for feature in features)  # ToDo посчитать и вернуть интегральный показатель
