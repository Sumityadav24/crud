from django.shortcuts import render, HttpResponseRedirect
from . forms import Student
from . models import User

# Create your views here.


def add_show(request):
    if request.method == "POST":
        fm = Student(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name=name, email=email, password=password)
            reg.save()
            fm = Student()
    else:
        fm = Student()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'data': stud})


def update(request, id):
    if request.method == "POST":
        a = User.objects.get(pk=id)
        fm = Student(request.POST, instance=a)
        if fm.is_valid():
            fm.save()
    else:
        a = User.objects.get(pk=id)
        fm = Student(instance=a)
    return render(request, 'enroll/update.html', {'form': fm})


# This fucntion will delete data from datatdbse
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
