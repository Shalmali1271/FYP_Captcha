from django.db import models

class Captcha(models.Model) :
    img = models.ImageField()
    key = models.CharField(max_length = 30)