from django.contrib import admin
from .models import Education,Teacher,Lesson,Rate,attendance
# Register your models here.
admin.site.register(Lesson)
admin.site.register(Education)
admin.site.register(Teacher)
admin.site.register(Rate)
admin.site.register(attendance)
