from django.db import models

# Create your models here.

class PaperStoreModel(models.Model):
    COURSES=(
         ('Math', 'Math'),
        ('Eng', 'Eng'),
        ('C++', 'C'),
        ('Java', 'Java'),
        ('Algorithm', 'Algorithm'),
        ('Data Structure', 'Data Structure'),
    )

    id = models.IntegerField(primary_key=True)
    student_Name = models.CharField(max_length=30)
    teacher_name = models.CharField(max_length=30)
    course_name = models.CharField(max_length=30, choices=COURSES)
    department_name= models.CharField(max_length=30)
    batch_name = models.CharField(max_length=30)
    Section_name= models.CharField(max_length=30)
    
