# Generated by Django 4.0.3 on 2022-08-19 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ajah', '0002_alter_course_work_subtopics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_work',
            name='subtopics',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
