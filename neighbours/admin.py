from django.contrib import admin
from .models import Hood,Calls

class HoodAdmin(admin.ModelAdmin):
    admin.site.register(Hood)
    admin.site.register(Calls)
