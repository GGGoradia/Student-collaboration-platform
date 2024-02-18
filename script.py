import serial
import webbrowser

# Replace 'COM3' with the appropriate serial port on your system
arduino = serial.Serial('/dev/cu.usbserial-0001', 9600)

while True:
    command = arduino.readline().strip()
    if command == b'DISPLAY_HTML':
        # Modify the path to your private HTML file
        html_file_path = 'http://localhost:8501/'
        webbrowser.open(html_file_path)  # Open the HTML file in the default web browser