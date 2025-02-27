from django.db import models


class Record(models.Model):

       creation_date = models.DateTimeField(auto_now_add=True)

       first_name = models.CharField(max_length= 25)

       last_name = models.CharField(max_length= 25)

       email = models.CharField(max_length= 50)

       phone = models.CharField(max_length= 15)

       address = models.CharField(max_length= 75)

       province = models.CharField(max_length= 55)

       country = models.CharField(max_length= 25)


       def __str__(self):
       
           return self.first_name + " " + self.last_name

