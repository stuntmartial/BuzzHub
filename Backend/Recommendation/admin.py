from django.contrib import admin
from .models import Suggestion,IgnoredSuggestions

class SuggestionAdmin(admin.ModelAdmin):
    list_display = [ 'suggestionId' , 'profile' , 'suggestionString' ]

class IgnoredSuggestionsAdmin(admin.ModelAdmin):
    list_display = [ 'ignoredId' , 'profile' , 'ignoredString' ]

admin.site.register(Suggestion,SuggestionAdmin)
admin.site.register(IgnoredSuggestions,IgnoredSuggestionsAdmin)