from django.contrib import admin
from shared.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'subject', 'is_read', 'created_at']
    search_fields = ['full_name', 'email', 'subject']
    list_filter = ['is_read', 'created_at']