from django.contrib import admin
from .models import Hitokoto

class HitokotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Hitokoto, HitokotoAdmin)
