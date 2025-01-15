from django.contrib import admin
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'address')  # Fields to display in the list view
    search_fields = ('name', 'size')  # Fields you can search for
    list_filter = ('size',)  # Add filter options in the admin panel

# Register the model with the custom admin class
admin.site.register(Users, UsersAdmin)