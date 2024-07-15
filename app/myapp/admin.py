from django.contrib import admin

# Register your models here.
from .models import ExampleModel,ContactMessage,Program

admin.site.register(ExampleModel)
admin.site.register(ContactMessage)
admin.site.register(Program)