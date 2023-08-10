from django.shortcuts import render
from django.http import HttpResponse

def main_index(request):
    return render(request, 'new_app/index.html')

def main_mon(request):
    return render(request, 'new_app/monday.html')

def main_tues(request):
    return render(request, 'new_app/tuesday.html')

def main_wed(request):
    return render(request, 'new_app/wednesday.html')

def main_thur(request):
    return render(request, 'new_app/thursday.html')

def main_fri(request):
    return render(request, 'new_app/friday.html')

def main_sat(request):
    return render(request, 'new_app/saturday.html')

def main_sun(request):
    return render(request, 'new_app/sunday.html')
