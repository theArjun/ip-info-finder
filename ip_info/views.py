from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):

    if request.method == 'POST':
        ip_address = str(request.POST.get('ip_address'))
        response = GeoIP2().city(ip_address)
        response['ip_address'] = ip_address
        return JsonResponse(response)

    else:
        return render(request, 'ip_info/index.html')
