from django.db import models

# Create your models here.
class Category(models.Model):
    ...

    class Meta:
        verbose_name_plural = "Categories"


class Hero(Entity):
    ...

    class Meta:
        verbose_name_plural = "Heroes"