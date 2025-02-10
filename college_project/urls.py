from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Importing views properly
from . import views
from . import hod_views
from . import staff_views
from . import student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.LOGIN, name='login'),
    path('dologin/', views.DOLOGIN, name='dologin'),
    path('dologout/', views.DOLOGOUT, name='dologout'),

    # Profile
    path('profile/', views.PROFILE, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # HOD Panel
    path('hod/home', hod_views.HOME, name='home'),
    path('hod/student/add', hod_views.ADD_STUDENT, name='add_student'),
    path('hod/student/view', hod_views.VIEW_STUDENT, name='view_student'),
    path('hod/student/edit/<str:id>', hod_views.Edit_STUDENT, name='edit_student'),
    path('hod/student/update', hod_views.UPDATE_STUDENT, name='update_student'),
    path('hod/student/delete/<str:admin>', hod_views.DELETE_STUDENT, name='delete_student'),

    # Staff
    path('hod/staff/add', hod_views.ADD_STAFF, name='add_staff'),
    path('hod/staff/view', hod_views.VIEW_STAFF, name='view_staff'),
    path('hod/staff/edit/<str:id>', hod_views.Edit_STAFF, name='edit_staff'),
    path('hod/staff/update', hod_views.UPDATE_STAFF, name='update_staff'),
    path('hod/staff/delete/<str:admin>', hod_views.DELETE_STAFF, name='delete_staff'),

    # Course
    path('hod/course/add', hod_views.ADD_COURSE, name='add_course'),
    path('hod/course/view', hod_views.VIEW_COURSE, name='view_course'),
    path('hod/course/edit/<str:id>', hod_views.Edit_COURSE, name='edit_course'),
    path('hod/course/update', hod_views.UPDATE_COURSE, name='update_course'),
    path('hod/course/delete/<str:id>', hod_views.DELETE_COURSE, name='delete_course'),

    # Subject
    path('hod/subject/add', hod_views.ADD_SUBJECT, name='add_subject'),
    path('hod/subject/view', hod_views.VIEW_SUBJECT, name='view_subject'),
    path('hod/subject/edit/<str:id>', hod_views.Edit_SUBJECT, name='edit_subject'),
    path('hod/subject/update', hod_views.UPDATE_SUBJECT, name='update_subject'),
    path('hod/subject/delete/<str:id>', hod_views.DELETE_SUBJECT, name='delete_subject'),

    # Session Year
    path('hod/session/add', hod_views.ADD_SESSION, name='add_session'),
    path('hod/session/view', hod_views.VIEW_SESSION, name='view_session'),
    path('hod/session/edit/<str:id>', hod_views.Edit_SESSION, name='edit_session'),
    path('hod/session/update', hod_views.UPDATE_SESSION, name='update_session'),
    path('hod/session/delete/<str:id>', hod_views.DELETE_SESSION, name='delete_session'),

    # Notification
    path('hod/staff/send_notification/', hod_views.STAFF_SEND_NOTIFICATION, name='staff_send_notification'),

    # Staff Panel
    path('staff/home', staff_views.STAFF_HOME, name='staff_home'),

    # Attendance
    path('staff/take_attendance', staff_views.TAKE_ATTENDANCE, name='take_attendance'),
    path('staff/save_attendance', staff_views.SAVE_ATTENDANCE, name='save_attendance'),
    path('staff/view_attendance', staff_views.VIEW_ATTENDANCE, name='view_attendance'),

    # Student Panel
    path('student/home', student_views.STUDENT_HOME, name='student_home'),
    path('student/view_attendance', student_views.STUDENT_VIEW_ATTENDANCE, name='student_view_attendance'),  # Fixed typo

]

# Serving Media files in Development & Production
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
