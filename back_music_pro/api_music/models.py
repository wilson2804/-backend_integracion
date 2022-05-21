import email
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import  PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """manager para perfiles de usuario"""
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Usuario debe tener email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ MODELO BASE DE DATOS PARA USUARIOS EN EL SISTEMA"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active =models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

class Marca(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class Modelo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500, null=False, blank=False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500, null=False, blank=False)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="sub_categoria",
        db_index=True,
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=500, unique=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False)
    precio = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class imagen(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=500)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False, blank=False,related_name="imagen")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)



