from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def lap_times(request):
    # Example: Get lap times for Lewis Hamilton in 2022 Bahrain GP
    response = requests.get("https://api.openf1.org/v1/lap_times", params={
        "year": 2022,
        "session_name": "R",
        "driver_number": 44  # Hamilton
    })

    lap_data = response.json()
    context = {
        'lap_times': lap_data[:20]  # limit for display
    }
    return render(request, 'f1statsapp/lap_times.html', context)