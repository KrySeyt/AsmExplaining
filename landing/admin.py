from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, DictionaryTerm


class DictionaryTermAdmin(admin.ModelAdmin):
    pass


admin.site.register(DictionaryTerm, DictionaryTermAdmin)
admin.site.register(User, UserAdmin)
