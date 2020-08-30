from django.contrib import admin
from .models import Questions, UserAnswer

# Register your models here.

admin.site.register(Questions)
admin.site.register(UserAnswer)

