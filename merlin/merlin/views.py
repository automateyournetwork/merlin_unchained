from django.shortcuts import render

from .models import ShowVersion

def year_archive(request, year):
    v_list = ShowVersion.objects.filter(timestamp__year=year)
    context = {'year': year, 'version_list': v_list}
    return render(request, 'ShowVersion/year_archive.html', context)