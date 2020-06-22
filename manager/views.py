from django.shortcuts import render,redirect
from .forms import AddStudent,TakeAttend
from django.contrib import messages
from .models import TakeAttendance, Students
from django.contrib.auth.decorators import login_required

def index(request): 
    return render(request, 'index.html')

@login_required
def addStudent(request):
    if request.method == 'POST':
        form = AddStudent(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'New Student has been added!!')
            return redirect('addStudent')
    else:
        form = AddStudent()
    return render(request, 'attendence/students.html',{'form':form})

@login_required
def addAttendence(request):
    if request.method == "POST":
        form = TakeAttend(request.POST) 
        if form.is_valid():
            form.save()
            # instance = form.save(commit=False)
            # instance.owner ssss= request.user
            # instance.id = request.user.id
            # instance.email = request.user.email
            # instance.save()     
            # title = form.cleaned_data.get('title')        
            messages.success(request, f'Attendence Is Added')
            return redirect('addAttendence')
    else:
        form = TakeAttend()
    return render(request,'attendence/take_attendence.html', {'form':form})

@login_required
def listAttendence(request):
    all_uploads = TakeAttendance.objects.all()
    return render(request, 'attendence/list_attendence.html',{'uploads':all_uploads})

@login_required
def check(request):
    obj = TakeAttendance.objects.all()
    list_subject = [
        'Database Management',
        'Engineering Drawing',
        'Web Technology',
        'Advance Java',
        'Dot Net Technology'
    ]
    list_subject_short = [
        'DBMS',
        'EG',
        'WT',
        'AJ',
        '.NET'
    ]
    args = {'obj':obj,'list_subject_short':list_subject_short,'list_subject':list_subject}
    return render(request,'attendence/check.html',args)
    
@login_required
def subject(request):
    return render(request, 'attendence/subject_attendence.html')

@login_required
def dynamic_lookup_view(request, subject):
    # obj = Donate.objects.get(id=subject)
    obj = TakeAttendance.objects.all().filter(subject=subject)
    subject_name = subject

    args = {'obj':obj, 'subject_name':subject_name}
    return render(request, 'attendence/subject_attendence.html',args)

def delete(request, id):
    attendance_data = TakeAttendance.objects.get(id=id)
    attendance_data.delete()
    return redirect('check')

# def edit(request, id):
#     attendance_data = TakeAttendance.objects.get(id=id)
#     args = {'attendance_data': attendance_data}
#     return render(request,'attendence/edit.html',args)


# def update(request, id):
#     attendance_data = TakeAttendance.objects.get(id=id)

#     if request.method == "POST":
#         form = TakeAttend(request.POST, instance=attendance_data) 
#         if form.is_valid():
#             form.save()
#             # instance = form.save(commit=False)
#             # instance.owner ssss= request.user
#             # instance.id = request.user.id
#             # instance.email = request.user.email
#             # instance.save()     
#             # title = form.cleaned_data.get('title')        
#             messages.success(request, f'Attendence Is Updated')
#             return redirect('check')
#     return render(request,'attendence/edit.html', {'attendance_data':attendance_data})


def update(request, id):  
    attendance_data = TakeAttendance.objects.get(id=id)
    form = TakeAttend(request.POST, instance=attendance_data) 
    if form.is_valid():  
        form.save()  
        messages.success(request, f'Attendence Is Updated')
        return redirect("check")  
    return render(request, 'attendence/update.html', {'form':form,'attendance_data':attendance_data})