from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.IntegerField()
    birthday = models.DateField()
    gpax = models.DecimalField(max_digits=3, decimal_places=2)
    
    def __unicode__(self):
        return self.fname + " " + self.lname + " [ " + str(self.gpax) + " ]"