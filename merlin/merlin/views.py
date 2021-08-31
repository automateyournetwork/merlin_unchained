from django.shortcuts import render

from .models import ShowVersion

def year_archive(request, year):
    v_list = ShowVersion.objects.filter(timestamp__year=year)
    context = {'year': year, 'version_list': v_list}
    return render(request, 'ShowVersion/year_archive.html', context)

def month_archive(request, year, month):
    v_list = ShowVersion.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'version_list': v_list}
    return render(request, 'ShowVersion/month_archive.html', context)

def day_archive(request, year, month, day):
    v_list = ShowVersion.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'version_list': v_list}
    return render(request, 'ShowVersion/day_archive.html', context)

def os_archive(request, os):
    v_list = ShowVersion.objects.filter(os=os)
    context = {'os': os, 'version_list': v_list}
    return render(request, 'ShowVersion/os_archive.html', context)