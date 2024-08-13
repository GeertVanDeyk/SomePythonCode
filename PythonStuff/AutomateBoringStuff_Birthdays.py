birthdays_dict = { 'Isaura' : '20030924', 'Kathleen' : '19740411'}

def dump_birthdays_dict():
    for all_keys, all_values in birthdays_dict.items():
        print('The birthday of ' + all_keys + ' is on ' + all_values)

def update_birthdays_dict(name):
    print('''I don't know the birthday of ''' + name)
    dayOfBirth = input('Enter the birthday of ' + name + ' : ')
    if dayOfBirth == '':
       print('''Sorry, I can't help you''')
    else:
       birthdays_dict[name] = dayOfBirth
       print('Ok, I have noted that the birthday of ' + name + ' is on ' + birthdays_dict[name])
      
def print_birthday(name):
    print('The birthday of ' + name + " is on " + str(birthdays_dict[name]))

def end_of_birthday_planner():
    print()
    print('Bye now, have a great day')
    if len(birthdays_dict) > 0:
        print ('\nREMEMBER : \n')
        dump_birthdays_dict() 




while True:
    name = input('Enter a name (just press enter to quit): ')
    if name == '':
        end_of_birthday_planner()
        break
    elif name in birthdays_dict:
        print_birthday(name)
    else :
        update_birthdays_dict(name)
           
            
