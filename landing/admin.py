from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, DictionaryTerm
from .forms import DictionaryTermAdminForm


@admin.register(DictionaryTerm)
class DictionaryTermAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    form = DictionaryTermAdminForm


admin.site.register(User, UserAdmin)
