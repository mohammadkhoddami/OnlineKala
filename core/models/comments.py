from django.db import models
from django.contrib.auth import get_user_model


from .base import BaseModel
from .product import Product


class Comment(BaseModel):
    COMMENT_STATUS = [
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('notapproved', 'NotApproved')
    ]
    
    #relation forigen keys
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments'
    )#User.comments.all()
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comment'
    )#Product.comment.all()
    body = models.TextField()
    status = models.CharField(max_length=15, choices=COMMENT_STATUS, default=COMMENT_STATUS[0][0])
    
    
    def __str__(self):
        return f'{self.author.first_name} - {self.author.last_name} write {self.body} and status is: {self.status}'
    
    