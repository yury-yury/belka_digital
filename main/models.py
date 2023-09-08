from django.db import models

from users.models import User


class OreSample(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=300)
    iron_content = models.FloatField()
    silicon_content = models.FloatField()
    aluminum_content = models.FloatField()
    calcium_content = models.FloatField()
    sulfur_content = models.FloatField()

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Проба концентрата"
        verbose_name_plural: str = "Пробы концентрата"
