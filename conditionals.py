mark = input('Enter mark: ')
mark= int(mark)
if mark == 65:
    print('Pass')
elif mark < 75 and mark > 65:
    print('Merit')
elif mark > 85 :
    print('Distinction')
else:
    print('Fail')