from django.contrib import admin
from paper.models import PaperStoreModel
# Register your models here.

class PaperStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id','student_Name', 'teacher_name', 'course_name', 'department_name',
                    'batch_name', 'Section_name', 'paper'
                    )
    
admin.site.register(PaperStoreModel,PaperStoreModelAdmin)

