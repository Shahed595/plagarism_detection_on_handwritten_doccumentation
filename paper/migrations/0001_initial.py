# Generated by Django 4.2.1 on 2023-07-25 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaperStoreModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_Name', models.CharField(max_length=30)),
                ('teacher_name', models.CharField(max_length=30)),
                ('course_name', models.CharField(choices=[('Math', 'Math'), ('Eng', 'Eng'), ('C++', 'C'), ('Java', 'Java'), ('Algorithm', 'Algorithm'), ('Data Structure', 'Data Structure')], max_length=30)),
                ('department_name', models.CharField(max_length=30)),
                ('batch_name', models.CharField(max_length=30)),
                ('Section_name', models.CharField(max_length=30)),
            ],
        ),
    ]
