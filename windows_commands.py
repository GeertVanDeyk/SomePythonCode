import subprocess

# for processes that can be run from 'Run' or 'Uitvoeren'
#this example prints the output of a ping command
print(subprocess.getoutput('ping 15.134.159.11'))

# for processes that must be run from cmd
#this example does the following:
## 1. opens the windows cmd
myprocess = subprocess.Popen('cmd')
## 2. captures the output (and further puts it in a list for editing)
list_myoutput = str(subprocess.getoutput('net use')).splitlines()
print(list_myoutput[6:-1:])
## 3. ends the process closing the windows cmd window
myprocess.terminate()

    
