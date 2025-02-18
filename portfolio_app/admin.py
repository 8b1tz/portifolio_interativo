from django.contrib import admin

from .models import Interesse, Projeto, UserProfile

admin.site.register(UserProfile)
admin.site.register(Projeto)
admin.site.register(Interesse)
