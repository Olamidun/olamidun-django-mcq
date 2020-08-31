from django.contrib import admin
from .models import Questions, Quiz, QuizTaker

# Register your models here.


class QuizTakerAdmin(admin.ModelAdmin):
    list_display = ['quiz_taker', 'score']
    list_display_links = ['quiz_taker', 'score']
    search_fields = ['quiz_taker__username']


admin.site.register(Questions)
admin.site.register(Quiz)
admin.site.register(QuizTaker, QuizTakerAdmin)

