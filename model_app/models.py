from django.db import models


# Create your models here.
class Students(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length =20)
    emailaddress = models.EmailField(max_length=20)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    def __str__(self) :
        return f'{self.FirstName} {self.LastName}'
    class Meta:
        db_table = 'wanafunzi'

class Teachers(models.Model):  
    firstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length =20)
    emailaddress = models.EmailField(max_length=20)
    def __str__(self) :
        return f"{self.firstName} {self.LastName}"

class Parents(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length =20)
    emailaddress = models.EmailField(max_length=20)
    phone_number = models.CharField(max_length=15)
    def __str__(self) :
        return  f"{self.FirstName} {self.LastName}"
    
class Host(models.Model):
    title = models.CharField(max_length = 40)
    description = models.TextField(max_length = 255)
    author = models.CharField(max_length = 20)
    created_at = models.DateTimeField()
    def __str__(self):
        return f'{self.title}  by {self.author} on  {self.created_at}'




