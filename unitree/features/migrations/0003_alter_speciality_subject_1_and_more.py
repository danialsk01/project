# Generated by Django 4.2.1 on 2023-05-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_rename_professions_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='subject_1',
            field=models.CharField(choices=[('biology', 'Biology'), ('geography', 'Geography'), ('creative exam', 'Creative exam'), ('the World History', 'The World History'), ('mathematics', 'Mathematics'), ('physics', 'Physics'), ('informatics', 'Informatics'), ('chemistry', 'Chemistry'), ('kazakh language', 'Kazakh language'), ('kazakh literature', 'Kazakh literature'), ('russian language', 'Russian language'), ('russian literature', 'Russian literature'), ('foreign language', 'Foreign language'), ('law basics', 'Law basics')], max_length=20),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='subject_2',
            field=models.CharField(choices=[('biology', 'Biology'), ('geography', 'Geography'), ('creative exam', 'Creative exam'), ('the World History', 'The World History'), ('mathematics', 'Mathematics'), ('physics', 'Physics'), ('informatics', 'Informatics'), ('chemistry', 'Chemistry'), ('kazakh language', 'Kazakh language'), ('kazakh literature', 'Kazakh literature'), ('russian language', 'Russian language'), ('russian literature', 'Russian literature'), ('foreign language', 'Foreign language'), ('law basics', 'Law basics')], max_length=20),
        ),
    ]
