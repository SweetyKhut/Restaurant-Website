from statistics import mode
from django.contrib.auth.models import User
from email.mime import image
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
# Create your models here.
    
class Restaurant(models.Model):
    name = models.CharField(_("name") ,max_length = 255)
    area = models.CharField(_("area"), max_length = 255)
    cuisines = models.CharField(_("cuisines"), max_length = 255)
    cost_for_Two = models.BigIntegerField(_("costForTwo"))
    address = models.CharField(_("address"), max_length = 255)
    locality = models.CharField(_("locality"), max_length = 25)
    avgRating = models.FloatField(_("avgRating"), max_length = 25)
    picture = models.ImageField(upload_to = "static/images/" , default = "/static/images/dess1.png")
    desciption = models.CharField(blank=True, null =True, max_length = 500)
    
    
    def __str__(self):
        return self.name   
    
    class Meta:
        db_table = "rest_data"
        
class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    name = models.ForeignKey(Restaurant, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(max_length = 250, blank = True, null=True)
    stars = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content


    
    