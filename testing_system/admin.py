from django.contrib import admin
from .models import Question, Test, Discipline

# Register your models here.


admin.site.register(Question)
admin.site.register(Test)
admin.site.register(Discipline)