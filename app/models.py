from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Nombre debe tener al menos 2 caracteres";
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Nombre debe tener al menos 2 caracteres";
        if not SOLO_LETRAS.match(postData['first_name']):
            errors['solo_letras_first_name'] = "Solo letras en el nombre por favor"
        if not SOLO_LETRAS.match(postData['last_name']):
            errors['solo_letras_last_name'] = "Solo letras en el apellido por favor"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Correo invalido"
        if len(postData['password']) < 8:
            errors['password'] = "Contraseña debe tener al menos 8 caracteres";
        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "Las Contraseñas no coinciden"        
        return errors

class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

class MensajeManager(models.Manager):
    def validador_mensaje(self, postData):
        errors = {}
        if len(postData['mensaje']) < 4:
            errors['mensaje'] = "El mensaje debe tener al menos 4 caracteres";
        return errors

class Mensaje(models.Model):
    mensaje = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="id_mensaje", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = MensajeManager()

    def __str__(self):
        return f"{self.mensaje}"

    def __repr__(self):
        return f"{self.mensaje}"

class ComentarioManager(models.Manager):
    def validador_comentario(self, postData):
        errors = {}
        if len(postData['comentario']) < 2:
            errors['comentario'] = "El comentario debe tener al menos 2 caracteres";
        return errors

class Comentario(models.Model):
    comentario = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="comentarios", on_delete = models.CASCADE)
    mensaje = models.ForeignKey(Mensaje, related_name="comentarios", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = ComentarioManager()

    def __str__(self):
        return f"{self.comentario}"

    def __repr__(self):
        return f"{self.comentario}"

