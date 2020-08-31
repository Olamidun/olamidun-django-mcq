from django.contrib import admin
from .models import Questions, UserScore

# Register your models here.


class UserScoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'score']
    list_display_links = ['user', 'score']
    search_fields = ['user__username']


admin.site.register(Questions)
admin.site.register(UserScore, UserScoreAdmin)

