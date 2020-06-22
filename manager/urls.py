from django.urls import path,include
from manager import views

urlpatterns = [
    path('addStudent/', views.addStudent,name='addStudent'),
    path('addAttendence/', views.addAttendence,name='addAttendence'),
    path('listAttendence/',views.listAttendence, name='listAttendence'),
    path('check/',views.check,name='check'),
    path('subject/',views.subject,name="subject"),
    path('subject/<str:subject>',views.dynamic_lookup_view, name='subject'),
    path('delete/<int:id>',views.delete, name='delete'),
    # path('edit/<int:id>',views.edit, name='edit'),
    path('update/<int:id>',views.update, name='update'),
]
