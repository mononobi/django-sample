from django.db import models


class CarPrice(models.Model):

    id = models.IntegerField(db_column='id', primary_key=True, auto_created=True)
    price = models.FloatField(db_column='price')

    def __str__(self):
        return f'{self.id}:{self.price}'


class Car(models.Model):

    id = models.IntegerField(db_column='id', primary_key=True, auto_created=True)
    company = models.CharField(db_column='company', max_length=60)
    model = models.CharField(db_column='model', max_length=60)
    product_year = models.IntegerField(db_column='product_year')
    price = models.ForeignKey(CarPrice, on_delete=str)

    def __str__(self):
        return f'{self.id}:{self.company}.{self.model}.{self.product_year}'
