from django.contrib import admin

# Register your models here.
from .models import LisenseData


@admin.register(LisenseData)
class LisenseDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnic', 'city')

