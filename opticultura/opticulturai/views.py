from django.http import HttpResponse
from django.shortcuts import render
import serial.tools.list_ports
import sys, time


def opticultura_view(request):
    return HttpResponse("Hello, World!")


def home_view(request):
    return render(request, 'main.html')

def discover_view(request):
    return render(request, 'discover.html')

def settings_view(request):
    return render(request, 'settings.html')

def led_view(request):
    return render(request, 'led.html')

def led_control(request):
    if request.method == 'POST':
        print(request.POST)

        red = int(request.POST.get('red_intensity', 0))
        green = int(request.POST.get('green_intensity', 0))
        blue = int(request.POST.get('blue_intensity', 0))

        serialInst = serial.Serial()
        com = 4

        serialInst.baudrate = 9600
        serialInst.port = "COM4"
        serialInst.open()
        command = "BLUE"
        time.sleep(2)
        serialInst.write(f"{red},{green},{blue}\n".encode())
    return render(request, 'led.html')