from django.contrib import admin

from .models import HighLevel

@admin.register(HighLevel)
class HighAdmin(admin.ModelAdmin):
    list_display = ['h_id', 'name']
    readonly_fields = ("h_id","created_at")
    fieldsets = [
        ('Data', {
            'fields':('h_id', 'name', 'is_active', 'description', 'created_at')
        })
        ]
