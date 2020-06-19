from datetime import datetime
def repeating_code(task_name):
    print(task_name)
    print(datetime.now())
    print()

   
repeating_code('hi')
for x in range(0,9):
    print(x)
repeating_code('loop completed')

#mailid genarting
def getCode(name):
    first_name_letter1=first_name[0:1].lower()
    #last_name_letter2=last_name[0:5]
    return first_name_letter1

first_name=input('Enter your first name: ')
name1=getCode(first_name)
last_name=input('Enter your Last name: ')
name2=getCode(last_name)

print('your email id for the college is :  ' + name1 + last_name + '1@leomail.tamuc.edu')