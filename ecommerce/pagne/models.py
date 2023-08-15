from django.db import models

# Create your models here.
class categorie(models.Model):
    Libele=models.CharField(max_length=50)
    Date_Ajout=models.DateTimeField(auto_now=True)
    slug=models.SlugField(max_length=50)
    class Meta:
        ordering = ['-Date_Ajout']

    def __str__(self):
        return self.Libele

class pagne(models.Model):
    Libele=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)
    prix=models.IntegerField()
    Date_Ajout=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='img_update', blank=True,null=True)
    Categorie=models.ForeignKey(categorie,related_name='categorie',on_delete=models.CASCADE)
    class Meta:
        ordering = ['-Date_Ajout']

    def __str__(self):
        return self.Libele