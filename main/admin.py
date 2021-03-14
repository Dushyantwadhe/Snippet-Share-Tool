from django.contrib import admin
from main.models import TextSnippet, SecretKey

# Register your models here.


admin.site.register(TextSnippet)
admin.site.register(SecretKey)
