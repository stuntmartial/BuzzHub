from django.contrib import admin
from .models import Relationship

class RelationshipAdmin(admin.ModelAdmin):
    list_display = [
        'entity1',
        'entity2',
        'sender',
        'connection_status'
    ]

admin.site.register(Relationship,RelationshipAdmin)