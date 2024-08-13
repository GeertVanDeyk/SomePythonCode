import subprocess

# for processes that must be run from cmd
#this example does the following:
## 1. opens the windows cmd
myprocess = subprocess.Popen('cmd')
## 2. captures the output (and further puts it in a list for editing)
list_myoutput = str(subprocess.getoutput('help')).splitlines()
for element in list_myoutput:
    print(element)
## 3. ends the process closing the windows cmd window
myprocess.terminate()
