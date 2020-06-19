
city=input('enter your city:')
tax=0
if(city=='abc'):
    output1=input('enter your country name:')
    if(output1=='canada') or (output1=='mexico'):
        print('welcome to canada')
        tax=0.75
    if output1 in('USA','India','Aus'):
        tax=1.2
    if(output1=='africa'):
        tax=1.5
else:
    tax=0.0
print(tax)