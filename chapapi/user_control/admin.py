from django.contrib import admin
from .models import CustomUser , Jwt

# Register your models here.

#  utilisé dans les applications Web Django pour enregistrer un modèle utilisateur personnalisé auprès du site d'administration Django.
admin.site.register((CustomUser , Jwt))
