from django.db import models

class Post(models.Model):
    post_date = models.DateField(auto_now_add=True) 
    specie = models.CharField(max_length = 30)
    pet_name = models.CharField(max_length = 30)
    author = models.ForeignKey("User", on_delete = models.CASCADE)
    comuna = models.ForeignKey("Comuna", on_delete = models.PROTECT)
    description = models.TextField(max_length = 1000)
    breed = models.CharField(max_length = 50)
    sex = models.CharField(choices = [('MA', 'Macho'), ('HE', 'Hembra')])
    pet_size = models.CharField(choices = [('GR', 'Grande'), ('ME', 'Mediano'), ('PE', 'Pequeño')])
    parasytes = models.CharField(choices = [('SI', 'Sí'), ('NO', 'No')])
    sterilized =  models.CharField(choices = [('SI', 'Sí'), ('NO', 'No'), ('DS', 'Desconocido')])
    vaccinated = models.CharField(choices = [('SI', 'Sí'), ('NO', 'No'), ('DS', 'Desconocido')])

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    image = models.ImageField()
