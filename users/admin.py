from django.contrib import admin

# Register your models here.
from .models import SubscribedUser


class UserAdmin(admin.ModelAdmin):    
    search_fields = ['name','email']
    list_display = ('name','email',)
    list_per_page = 10
    list_max_show_all = 50
    
admin.site.register(SubscribedUser, UserAdmin)