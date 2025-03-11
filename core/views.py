from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.contrib import messages
from .models import Student
from .forms import AddStudentForm

# Home Page View


class Home(View):
    def get(self, request):
        try:
            student_data = Student.objects.all()
            return render(request, 'core/home.html', {'studata': student_data})
        except Exception as e:
            messages.error(
                request, "Something went wrong while fetching data.")
            return HttpResponseServerError("Internal Server Error")

# Add Student View


class Add_Student(View):
    def get(self, request):
        fm = AddStudentForm()
        return render(request, 'core/add-student.html', {'form': fm})

    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():  # Fixed missing parentheses
            try:
                fm.save()
                messages.success(request, "Student added successfully!")
                return redirect('/')
            except Exception as e:
                messages.error(request, "An error occurred while saving data.")
                return HttpResponseServerError("Internal Server Error")
        else:
            messages.warning(request, "Invalid form submission.")
            return render(request, 'core/add-student.html', {'form': fm})

# Delete Student View


class Delete_Student(View):
    def post(self, request):
        id = request.POST.get('id')
        if not id:
            return HttpResponseBadRequest("Invalid request: Missing student ID")

        try:
            studata = get_object_or_404(Student, id=id)
            studata.delete()
            messages.success(request, "Student deleted successfully!")
        except Exception as e:
            messages.error(
                request, "An error occurred while deleting the student.")
            return HttpResponseServerError("Internal Server Error")

        return redirect('/')

# Edit Student View


class Edit_Student(View):
    def get(self, request, id):
        try:
            stu = get_object_or_404(Student, id=id)
            fm = AddStudentForm(instance=stu)
            return render(request, 'core/edit-student.html', {'form': fm})
        except Exception as e:
            messages.error(request, "Student not found or an error occurred.")
            return HttpResponseBadRequest("Invalid request")

    def post(self, request, id):
        try:
            stu = get_object_or_404(Student, id=id)
            fm = AddStudentForm(request.POST, instance=stu)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Student updated successfully!")
                return redirect('/')
            else:
                messages.warning(request, "Invalid form submission.")
                return render(request, 'core/edit-student.html', {'form': fm})
        except Exception as e:
            messages.error(request, "An error occurred while updating data.")
            return HttpResponseServerError("Internal Server Error")
