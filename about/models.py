from django.db import models

# Create your models here.

class About(models.Model):
    page = models.CharField(max_length=100)
    pageUrl = models.CharField(max_length=100)
    tips = models.CharField(max_length=200)
    content1 = models.CharField(max_length=500)
    content2 = models.CharField(max_length=500)
    content3 = models.CharField(max_length=500)
    content4 = models.CharField(max_length=500)
    publishDay = models.DateField()

    def __str__(self):
        return '<About:id' + str(self.id) + ',' + self.page + '(' + str(self.pageUrl) + ')>'