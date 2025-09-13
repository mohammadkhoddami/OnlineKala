from django.db import models

from core.models.base import BaseModel



class Order(BaseModel):
    STATUS_CHOICE = [
        ('unpaid', 'unpaid'),
        ('paid', 'paid'),
        ('cancel', 'cancel')
    ]
        
    customer = models.ForeignKey('core.Customer',
                                 on_delete=models.CASCADE,
                                 related_name='orders')#Customer.orders.all()
    status = models.CharField(max_length=8, choices=STATUS_CHOICE,
                              default=STATUS_CHOICE[0][0])
    

class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )#Order.items.all()
    product = models.ForeignKey(
        'core.Product',
        on_delete=models.CASCADE,
        related_name='ordered'
    )#Product.ordered.all()
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = [['order', 'product']]
    