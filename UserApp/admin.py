from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserDB)
admin.site.register(LawyerDB)
admin.site.register(BookDB)
admin.site.register(MsgDB)