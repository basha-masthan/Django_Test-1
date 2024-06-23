from django.contrib import admin

# Register your models here.
from .models import usrData,Course

admin.site.register(usrData)

admin.site.register(Course)
