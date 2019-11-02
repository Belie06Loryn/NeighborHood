from django.db import models
from django.contrib.auth.models import User

class Calls(models.Model):
    namecall = models.CharField(max_length =3000)
    fone = models.CharField(max_length =3000)

    def save_call(self):
        self.save()

    def dele_call(self):
        self.delete()    

class Hood(models.Model):
    image = models.ImageField(upload_to = 'photos/',null=True)
    name = models.CharField(max_length =6000)
    location = models.CharField(max_length =6000)
    count = models.CharField(max_length =6000)
    calls = models.ForeignKey(Calls, null=True) 

    def save_hood(self):
        self.save()

    def dele_hood(self):
        self.delete() 

    @classmethod
    def hood_by_id(cls,id):
        found = cls.objects.filter(id = id)
        return found

    @classmethod
    def update_hood(cls,id):
        imaje = cls.objects.filter(id=id).update(id=id)
        return imaje          
 
    @classmethod
    def searchs(cls,search):
        location = cls.objects.filter(location__icontains=search)
        return location