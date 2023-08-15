from django.contrib import admin
from .models import categorie,pagne
# Register your models here.
admin.site.register(categorie)
admin.site.register(pagne)
class AdminCategory(admin.ModelAdmin):
    list_display= ('libele','Date_Ajout')

class AdminPagne(admin.ModelAdmin):
    list_display= ('libele','prix','Date_Ajout','Categorie')