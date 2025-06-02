from django.db import models
from .base import BaseModel



class Product(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    categoory = models.ForeignKey('core.Category',on_delete=models.CASCADE, related_name='products')
    price = models.FloatField() #Decimal
    body = models.TextField()
    stash = models.IntegerField()
    active = models.BooleanField(default=True)
    #pictue 