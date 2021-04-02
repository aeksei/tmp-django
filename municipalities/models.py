from django.db import models


class ActivityField(models.Model):
    """ Абстрактный класс, описывающий сферы деятельности для муниципальных округов и районов """
    medicine = models.PositiveIntegerField(verbose_name="Медицина", blank=True, null=True)
    education = models.PositiveIntegerField(verbose_name="Образование", blank=True, null=True)
    communal_services = models.PositiveIntegerField(verbose_name="ЖКХ", blank=True, null=True)
    ...  # ToDo other Activity fields

    class Meta:
        abstract = True


class MunicipalityIntegralIndicator(ActivityField):
    """ Класс, содержащий интегральные показатели сфер деятельности муниципальных округов """
    municipality = ...  # ToDo ForeignKey

    class Meta:
        verbose_name = "Интегральный показатель муниципального округа"
        verbose_name_plural = "Интегральные показатели муниципальных округов"
