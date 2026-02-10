from django.contrib import admin
from .models import MyDiary
# Register your models here.
class MyDiaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'date')
    search_fields = ('title',)
    
admin.register(MyDiary)
    