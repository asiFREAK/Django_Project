from django.contrib import admin
from new_app.models import Student,Clasroom,Teachers,Marks

# Register your models here.
admin.site.register(Student)
admin.site.register(Clasroom)
admin.site.register(Teachers)
admin.site.register(Marks)