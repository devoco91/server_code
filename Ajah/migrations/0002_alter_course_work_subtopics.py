# Generated by Django 4.0.3 on 2022-08-19 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ajah', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_work',
            name='subtopics',
            field=models.TextField(null=True),
        ),
    ]
