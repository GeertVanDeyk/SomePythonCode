import sys
def splitList(anyList):
    try:
        for index in range(len(anyList)-1):
            print (anyList[index], end=', ')
        print (anyList[-1])

    except:
        the_type, the_value, the_traceback = sys.exc_info()
        print (the_type, the_value)
    finally:
        print(anyList, ' is a list with ',(str)(len(anyList)),'elements')    
spam = ['apples','bananas','tofu','cats']
splitList(spam)
eggs = []
splitList(eggs)
