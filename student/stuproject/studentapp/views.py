from django.shortcuts import render, redirect
from .models import Student

def student_form(request):
    message = ""
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            roll_number=request.POST['roll'],
            student_class=request.POST['class'],
            age=request.POST['age'],
            parent_contact=request.POST['contact']
        )
        message = "Student added successfully"
    return render(request, 'studentapp/student_form.html', {'message': message})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentapp/students_list.html', {'students': students})


def student_update(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.roll_number = request.POST['roll']
        student.student_class = request.POST['class']
        student.age = request.POST['age']
        student.parent_contact = request.POST['contact']
        student.save()
        return redirect('/studentapp/list/')

    return render(request, 'student_update.html', {'student': student})


def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/studentapp/list/')