from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import *


class BCourseForm(ModelForm):
	class Meta:
		model = Course_Work
		fields ='__all__'

class BAttendanceForm(ModelForm):
	class Meta:
		model = Attendance
		fields ='__all__'

class BGradeForm(ModelForm):
	class Meta:
		model = Grade
		fields ='__all__'