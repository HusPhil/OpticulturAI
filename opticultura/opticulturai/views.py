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

def find_arduino_uno_port():
    # Get a list of all available serial ports
    ports = serial.tools.list_ports.comports()
    
    # Iterate through the list of ports and check if any of them correspond to Arduino Uno
    for port in ports:
        if "Arduino Uno" in port.description:
            return port.device
    
    # If Arduino Uno is not found, return None
    return None

def led_control(request):
    if request.method == 'POST':
        print(request.POST)

        red = int(request.POST.get('red_intensity', 0))
        green = int(request.POST.get('green_intensity', 0))
        blue = int(request.POST.get('blue_intensity', 0))

        # Find the COM port where Arduino Uno is connected
        arduino_port = find_arduino_uno_port()

        if arduino_port:
            # Initialize and open serial connection
            serialInst = serial.Serial()
            serialInst.baudrate = 9600
            serialInst.port = arduino_port
            serialInst.open()

            # Send LED intensity values to Arduino
            command = "BLUE"  # Not sure what this command is for, adjust as needed
            time.sleep(2)  # Wait for Arduino to initialize
            serialInst.write(f"{red},{green},{blue}\n".encode())

            # Close the serial connection
            serialInst.close()
        else:
            print("Arduino Uno not found.")
    return render(request, 'led.html')