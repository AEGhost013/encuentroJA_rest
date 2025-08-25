from django.contrib import admin
# Register your models here.
from . import models

admin.site.register(models.Bam)
admin.site.register(models.Evento)
admin.site.register(models.Perfil)