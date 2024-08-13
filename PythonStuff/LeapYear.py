def is_leap(year):
    leap = False
    if year % 4 > 0:
        leap = False
    else:
        if year % 400 == 0:
            leap = False
        else:
            leap = True
    return leap


year = int(input())
print(is_leap(year))
