from django.contrib import admin
from .models import Fashion,Message
# Register your models here.

class MessageInline(admin.StackedInline):
    model = Message
    extra = 1


@admin.register(Fashion)
class FashionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'id']
    inlines = [MessageInline]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # search_fields = ['post']
    autocomplete_fields = ['post',]