from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'created_at')
    readonly_fields = ('user', 'created_at')
