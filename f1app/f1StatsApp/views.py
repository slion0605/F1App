from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import JsonResponse
# Create your views here.

def lap_times(request):
    # Example: Get lap times for Lewis Hamilton in 2022 Bahrain GP
    response = requests.get("https://api.openf1.org/v1/lap_times", params={
        "year": 2022,
        "driver_number": 1  # Hamilton
    })

    lap_data = response.json()
    context = {
        'lap_times': lap_data[:20]  # limit for display
    }
    return render(request, 'f1statsapp/lap_times.html', context)


def hamilton_monaco_race(request):

    response = requests.get("https://api.openf1.org/v1/drivers?driver_number=1&session_key=9158")
    data = response.json()
    print(response.url)

    return JsonResponse(data, safe=False)