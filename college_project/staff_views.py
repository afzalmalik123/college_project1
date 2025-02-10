from django.shortcuts import redirect,render,HttpResponse

from app.models import Subject, Staff, Session_Year, Student, Attendance, Attendance_Report


def STAFF_HOME(request):
    return render(request,'staff/staff_home.html')


def TAKE_ATTENDANCE(request):
    staff_id=Staff.objects.get(admin = request.user.id)

    subject =Subject.objects.filter(staff = staff_id)
    session_year=Session_Year.objects.all()
    action=request.GET.get('action')

    students = None
    get_subject = None
    get_session_year = None

    if action is not None:
        if request.method=='POST':
            subject_id=request.POST.get('subject_id')
            session_year_id=request.POST.get('session_year_id')

            get_subject=Subject.objects.get(id = subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)

            subject =Subject.objects.filter(id = subject_id)

            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id = student_id)

    context={
        'subject':subject,
        'session_year':session_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action,
        'students':students,
    }


    return render(request,'staff/take_attendance.html',context)


def SAVE_ATTENDANCE(request):
    if request.method=='POST':
        subject_id=request.POST.get('subject_id')
        session_year_id=request.POST.get('session_year_id')
        attendance_date=request.POST.get('attendance_date')
        student_id=request.POST.getlist('student_id')

        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_Year.objects.get(id=session_year_id)

        attendance=Attendance(
            subject_id=get_subject,
            attendance_date=attendance_date,
            session_year_id=get_session_year,
        )
        attendance.save()
        for i in student_id:
            stud_id = i
            int_stud = int(stud_id)

            p_student = Student.objects.get(id = int_stud)
            attendance_report=Attendance_Report(
                student_id=p_student,
                attendance_id=attendance,

            )
            attendance_report.save()

        return redirect('take_attendance')


def VIEW_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(staff_id = staff_id)
    session_year=Session_Year.objects.all()

    action=request.GET.get('action')

    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date=request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)
            attendance = Attendance.objects.filter(subject_id = get_subject)

            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id=attendance_id)

    context={
        'subject':subject,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'attendance_date':attendance_date,
        'attendance_report':attendance_report,
    }


    return render(request,'staff/view_attendance.html',context)