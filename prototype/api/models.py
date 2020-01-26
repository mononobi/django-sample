from django.db import models


class Car(models.Model):

    id = models.IntegerField(db_column='id', primary_key=True, auto_created=True)
    company = models.CharField(db_column='company', max_length=60)
    model = models.CharField(db_column='model', max_length=60)
    product_year = models.IntegerField(db_column='product_year')

    def __str__(self):
        return f'{self.model}.{self.product_year}.{self.id}'
