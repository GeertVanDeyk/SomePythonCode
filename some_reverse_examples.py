
def reverse_string_with_for (str_input) :
    str_output = ''
    for ch in str_input[len(str_input)::-1]:
        str_output += ch
    return str_output

def reverse_string_using_splices (str_input):
    return (str_input[::-1])

def check_palindroom(str_input = 'lepel'):
    return(reverse_string_with_for(str_input) == str_input)
    



    

if __name__ == '__main__':
    print( __file__, ' being called as standalone.')
    print(check_palindroom('racecar'))
    print(reverse_string_using_splices('Van Deyk'))
