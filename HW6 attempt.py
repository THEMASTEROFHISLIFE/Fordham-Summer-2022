Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======================== RESTART: /home/nicholas/HW6.py ========================
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/nicholas/HW6.py", line 17, in <module>
    import documentg.txt
ModuleNotFoundError: No module named 'documentg'
>>> 
======================== RESTART: /home/nicholas/HW6.py ========================
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/nicholas/HW6.py", line 19, in <module>
    with open('document.txt') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'document.txt'
>>> 
======================== RESTART: /home/nicholas/HW6.py ========================
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/nicholas/HW6.py", line 19, in <module>
    with open('documentg.txt') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'documentg.txt'
>>> 
======================== RESTART: /home/nicholas/HW6.py ========================
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/nicholas/HW6.py", line 23, in <module>
    with open('/home/nicholas.documentg.txt', 'r') as inp:
FileNotFoundError: [Errno 2] No such file or directory: '/home/nicholas.documentg.txt'
>>> 
==================================== RESTART: /home/nicholas/HW6.py ===================================
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/nicholas/HW6.py", line 28, in <module>
    import documentg.txt
ModuleNotFoundError: No module named 'documentg'
>>> 