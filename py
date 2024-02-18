Script started on Wed Nov  8 20:05:32 2023
[1m[7m%[27m[1m[0m                                                                                                                                                                       [0m[27m[24m[Jsuruchisingh@shubhams-MacBook-Air pythonProject1 % [K[?2004hppython script.py[?2004l
Traceback (most recent call last):
  File "/Users/suruchisingh/PycharmProjects/pythonProject1/venv/lib/python3.11/site-packages/serial/serialposix.py", line 322, in open
    self.fd = os.open(self.portstr, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^.py[?2004l
Traceback (most recent call last):
  File "/Users/suruchisingh/PycharmProjects/pythonProject1/venv/lib/python3.11/site-packages/serial/serialposix.py", line 322, in open
    self.fd = os.open(self.portstr, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 16] Resource busy: '/dev/cu.usbserial-0001'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/suruchisingh/PycharmProjects/pythonProject1/script.py", line 5, in <module>
    arduino = serial.Serial('/dev/cu.usbserial-0001', 9600)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/suruchisingh/PycharmProjects/pythonProject1/venv/lib/python3.11/site-packages/serial/serialutil.py", line 244, in __init__
    self.open()
  File "/Users/suruchisingh/PycharmProjects/pythonProject1/venv/lib/python3.11/site-packages/serial/serialposix.py", line 325, in open
    raise SerialException(msg.errno, "could not open port {}: {}".format(self._port, msg))
serial.serialutil.SerialException: [Errno 16] could not open port /dev/cu.usbserial-0ppython script.py[?2004l
Traceback (most recent call last):
  File "/Users/suruchisingh/PycharmProjects/pythonProject1/venv/lib/python3.11/site-packages/serial/serialposix.py", line 322, in open
    self.fd = os.open(self.portstr, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^y[?2004l
Traceback (most recent call last):
  File "/Users/suruchisingh/PycharmProjects/pythonProject1/venv/lib/python3.11/site-packages/serial/serialposix.py", line 322, in open
    self.fd = os.open(self.portstr, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 16] Resource busy: '/dev/cu.usbserial-0001'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/suruchisingh/PycharmProjects/pythonProject1/script.py", line 5, in <module>
    arduino = serial.Serial('/dev/cu.usbserial-0001', 9600)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/suruchisingh/PycharmProjects/pythonProject1/venv/lib/python3.11/site-packages/serial/serialutil.py", line 244, in __init__
    self.open()
  File "/Users/suruchisingh/PycharmProjects/pythonProject1/venv/lib/python3.11/site-packages/serial/serialposix.py", line 325, in open
    raise SerialException(msg.errno, "could not open port {}: {}".format(self._port, msg))
serial.serialutil.SerialException: [Errno 16] could not open port /dev/cu.usbserial-0001: [Errno 16] Resource busy: '/dev/cu.usbserial-0001'
[1m[7m%[27m[1m[0m                                                                                                                                                                       [0m[27m[24m[Jsuruchisingh@shubhams-MacBook-Air pythonProject1 % [K[?2004h001: [Errno 16] Resource busy: '/dev/cu.usbserial-0001'
[1m[7m%[27m[1m[0m                                                                                                                                                                       [0m[27m[24m[Jsuruchisingh@shubhams-MacBook-Air pythonProject1 % [K[?2004h