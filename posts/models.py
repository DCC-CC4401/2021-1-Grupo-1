from django.db import models

species = {'G': 'Gato',
           'P': 'Perro',
           'E': 'Erizo',
           'C': 'Conejo',
           'L': 'Loro',
           'TO': 'Tortuga',
           'TA': 'Tarantula',
           'O': 'Otro'}

class Post(models.Model):
    post_date = models.DateField(auto_now_add=True)
    specie = models.CharField(
        choices=species.items(),
        max_length=30)
    pet_name = models.CharField(max_length=30)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    comuna = models.ForeignKey("users.Comuna", on_delete=models.PROTECT)
    description = models.TextField(max_length=1000)
    breed = models.CharField(max_length=50, blank=True)
    sex = models.CharField(choices=[('MA', 'Macho'), ('HE', 'Hembra'), ('DS', 'Desconocido')], max_length=10)
    pet_size = models.CharField(choices=[('GR', 'Grande'), ('ME', 'Mediano'), ('PE', 'Pequeño')], max_length=10)
    parasytes = models.CharField(choices=[('SI', 'Sí'), ('NO', 'No')], max_length=10)
    sterilized = models.CharField(choices=[('SI', 'Sí'), ('NO', 'No'), ('DS', 'Desconocido')], max_length=10)
    vaccinated = models.CharField(choices=[('SI', 'Sí'), ('NO', 'No'), ('DS', 'Desconocido')], max_length=10)
    status = models.CharField(choices=[('Mío', 'Mío'), ('Calle', 'De la calle')], max_length=15)
    sighting_date = models.DateField(blank=True)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField()


class Interested(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='unique_interested')
        ]
