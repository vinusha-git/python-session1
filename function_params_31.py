#multiple params
def get_initials(name,uppercase1=True):
    if uppercase1:

      initial=name[0:1].upper()
    else:
      initial=name[0:1]

    return initial


first_name=input('Enter you first name: ')
first_name_pass=get_initials(first_name)
print('your initial is : ' +first_name_pass)
