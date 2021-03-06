from django.db import models
import os

# Fonctions for models

def path_and_rename(instance, filename):
    # upload_to = 'speedpost/images'
    ext = filename.split('.')[-1]
    nb = len(SpeedPost.objects.all())+1
    filename = "{}.{}".format(nb, ext)
    return os.path.join(upload_to, filename)

# Create your models here

class Categorie(models.Model):

    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Article(models.Model):

    upload_to = "articles/images"

    titre = models.CharField(max_length=100)
    contenu = models.TextField(max_length=None)

    preview = models.TextField(max_length=200)

    parution = models.DateField(auto_now=False, auto_now_add=True)
    last_modif = models.DateField(auto_now=True, auto_now_add=False)

    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    slug = models.CharField(max_length=30)

    # JEUX VIDEOS

    les_plus = models.TextField(max_length=None, blank=True)
    les_moins = models.TextField(max_length=None, blank=True)

    def __str__(self):
        return self.titre

    def path_and_rename(self, filename):
        upload_to = 'articles/images'
        mon_image = Image(filename, upload_to)
        return mon_image.path        

class SpeedPost(models.Model):

    contenu = models.TextField(max_length=200)
    parution = models.DateTimeField(auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to=path_and_rename, blank=True, null=True)

    def __str__(self):
        return self.contenu
    
    def path_and_rename(self, filename):
        upload_to = 'speedpost/images'
        mon_image = Image(filename, upload_to)
        return mon_image.path

class Lien(models.Model):

    nom_lien = models.TextField(max_length=None)
    lienHttp = models.TextField(max_length=None)

    def __str__(self):
        return self.nom_lien

class Image:

    mes_images = []

    def __init__(self, filename, location):

        self.nb = len(Image.mes_images)+1
        self.ext = filename.split('.')[1]
        self.filename = "{}.{}".format(nb, ext)

        self.folder = location
        self.path = os.path.join(self.folder, self.filename)

        Image.mes_images.append(self)

    def __repr__(self):
        return self.path

    def __del__(self):
        pass