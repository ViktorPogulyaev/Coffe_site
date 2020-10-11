from django.db import models

# Create your models here.

class BB(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата размещения')
    classification = models.ForeignKey('Classification', null=True, on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        verbose_name_plural = 'Объявлений'
        verbose_name = 'Объявление'
        ordering = ['price']

class Classification(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']