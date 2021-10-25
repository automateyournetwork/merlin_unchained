import csv, io
from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
from merlin.models import Devices

def device_upload(request):
    data = Devices.objects.all()

    prompt = {
        'order': 'Order of the CSV should be Hostname, Alias, Device Type, OS, Platform, Username, Password, Protocol, IP Address, Port, Connection Timeout',
        'profiles': data
    }

    if request.method == "GET":
        return render (request, "CSV_Upload/device_upload.html", prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload a correctly formatted .CSV file')
    
    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Devices.objects.update_or_create(
            hostname = column[0],
            alias = column[1],
            device_type = column[2],
            os = column[3],
            platform = column[4],
            username = column[5],
            password = column[6],
            protocol = column[7],
            ip_address = column[8],
            port = column[9],
            connection_timeout = column[10],
            timestamp=datetime.now().replace(microsecond=0)
        )
    context = {}
    return render(request, "CSV_Upload/device_upload.html", context)    