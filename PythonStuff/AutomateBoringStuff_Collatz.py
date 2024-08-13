import sys
def  CollatzSequence(anInt):
    if anInt%2 == 0:
        return (anInt//2)
    else:
        return (3 * anInt + 1)

 
try:
    used_value = (int) (input(' Enter an integer : '))
    while True:
         print (used_value)
         if used_value <= 1:
             break
         used_value = CollatzSequence(used_value)   
except:
    the_type, the_value, the_traceback = sys.exc_info()
    print (the_type, the_value)
    
    
