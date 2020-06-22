from .models import Students,TakeAttendance
from django import forms

class AddStudent(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('student_name','roll_no','semester','year')

class TakeAttend(forms.ModelForm):
    class Meta:
        model = TakeAttendance
        fields = ('roll','subject','date_time','time')
