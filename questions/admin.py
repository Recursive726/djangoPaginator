from django.contrib import admin
from .models import question

@admin.register(question)
class questionAdmin(admin.ModelAdmin):
	list_display = ('question_number', 'question_content','created_date')

