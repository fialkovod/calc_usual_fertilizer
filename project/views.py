from django.shortcuts import render


def calc(request):
    return render(request, 'project/project.html')