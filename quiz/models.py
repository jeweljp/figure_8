from __future__ import unicode_literals

from django.db import models

class level(models.Model):
    level = models.IntegerField(unique = True)
    ans = models.CharField(max_length = 50, null=False)

		
class fig(models.Model):
    """docstring for bells"""
    uname = models.CharField(max_length = 50, null=False,unique = True)
    level = models.IntegerField(default = 0)
    timeval =models.CharField(max_length = 400, null=True)
  	 