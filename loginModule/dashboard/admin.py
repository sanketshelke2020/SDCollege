from django.contrib import admin
from .models import UserExtended, Course, Notice
# Register your models here.
admin.site.register(Course)
admin.site.register(UserExtended)
admin.site.register(Notice)
