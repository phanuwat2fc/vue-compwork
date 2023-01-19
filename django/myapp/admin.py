from django.contrib import admin
from .models import Events,Member,Rank
# Register your models here.
class Madmin(admin.ModelAdmin):
    list_display = ['id','firstname', 'lastname', 'rank']

admin.site.register(Events)
admin.site.register(Member, Madmin)
admin.site.register(Rank)