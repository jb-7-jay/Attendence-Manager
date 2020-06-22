from django.db import models
from datetime import datetime, date

class Students(models.Model):

    student_name = models.CharField(max_length=80)
    roll_no = models.IntegerField(unique=True)
    class_name = models.CharField(max_length=80)
    semester = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return (f"{str(self.roll_no)} - {self.student_name}")

subject_choices = [
        ('DBMS','database Management'),
        ('EG','Engineering Drawing'),
        ('WT','Web Technology'),
        ('AJ','Advance Java'),
        ('.NET','Dot Net Technology'),
    ]

class TakeAttendance(models.Model):
    
    roll = models.ForeignKey(Students, related_name='books',default=None,on_delete=models.PROTECT)
    subject = models.CharField(choices = subject_choices,default='DBMS', max_length=6)
    date_time = models.DateField("Date(mm/dd/yyyy)",auto_now_add=False,default=datetime.now,auto_now=False)
    time = models.TimeField( auto_now=False, auto_now_add=False,default=datetime.now)

    def __str__(self):  
        return str(self.roll)
