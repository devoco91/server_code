from django.db import models

# Create your models here.


from django.db import models

# Create your models here.

class Course_Work(models.Model):
    cohort_id=models.CharField(max_length=200, blank=True)
    topic=models.CharField(max_length=200,null=True)
    subtopics=models.TextField(null=True)
    date_added=models.DateTimeField(auto_now_add=True)





class Attendance(models.Model):

    cohort_id=models.CharField(max_length=200, blank=True)
    names=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)


class Grade(models.Model):

    cohort_id=models.CharField(max_length=200, blank=True)
    serial_number=models.CharField(max_length=200, blank=True)
    name=models.CharField(max_length=1000,null=True)
    grade=models.CharField(max_length=1000,null=True)
    date_added=models.DateTimeField(auto_now_add=True)



