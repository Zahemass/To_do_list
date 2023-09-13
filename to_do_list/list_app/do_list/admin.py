from django.contrib import admin
from .models import to_do_list,name_list

# Register your models here.
admin.site.register(name_list)
admin.site.register(to_do_list)

