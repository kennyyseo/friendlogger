from django.contrib import admin
from .models import Friend, Meeting, Memory

# Register your models here.

admin.site.register(Friend)
admin.site.register(Meeting)
admin.site.register(Memory)
