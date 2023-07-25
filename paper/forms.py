from django import forms
from paper.models import PaperStoreModel
class PaperStoreForm(forms.ModelForm):
    class Meta:
        model = PaperStoreModel
        fields = ['id', 'student_Name', 'teacher_name', 'course_name', 'department_name', 'batch_name',
                    'Section_name','paper']
    