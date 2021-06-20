from django.db import models


class Post(models.Model):
    post_date = models.DateField(auto_now_add=True)
    specie = models.CharField(
        choices=[("G", "Gato"), ("P", "Perro"), ("E", "Erizo"), ("C", "Conejo"), ("L", "Loro"), ("TO", "Tortuga"),
                 ("TA", "Tarantula"), ("O", "Otro")],
        max_length=30)
    pet_name = models.CharField(max_length=30)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    comuna = models.ForeignKey("users.Comuna", on_delete=models.PROTECT)
    region = models.ForeignKey("users.Region", on_delete=models.PROTECT)
    description = models.TextField(max_length=1000)
    breed = models.CharField(max_length=50)  # aquí pasa lo mismo que con la especie
    sex = models.CharField(choices=[('MA', 'Macho'), ('HE', 'Hembra'), ('DS', 'Desconocido')], max_length=10)
    pet_size = models.CharField(choices=[('GR', 'Grande'), ('ME', 'Mediano'), ('PE', 'Pequeño')], max_length=10)
    parasytes = models.CharField(choices=[('SI', 'Sí'), ('NO', 'No')], max_length=10)
    sterilized = models.CharField(choices=[('SI', 'Sí'), ('NO', 'No'), ('DS', 'Desconocido')], max_length=10)
    vaccinated = models.CharField(choices=[('SI', 'Sí'), ('NO', 'No'), ('DS', 'Desconocido')], max_length=10)
    status = models.CharField(choices=[('Mío', 'Mío'), ('Calle', 'De la calle')], max_length=15)
    sighting_date = models.DateField(null=True)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField()
