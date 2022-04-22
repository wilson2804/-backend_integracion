from django.contrib import admin

# Register your models here.
from api_music import models

admin.site.register(models.UserProfile)
admin.site.register(models.Marca)
admin.site.register(models.Modelo)