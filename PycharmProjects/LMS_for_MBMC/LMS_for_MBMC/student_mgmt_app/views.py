from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #dictionary can be used to pass to the template engine as its context.
    context_dict = {'welcomeMessage': " I am bold font from the context"}

    # return HttpResponse("Student Management Application..")
    return render(request, 'student_mgmt_app/index.html', context_dict)
