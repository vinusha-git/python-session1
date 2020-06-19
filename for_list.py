from datetime import datetime

#listrange
# for name in['vinusha','janga','vinusha']:
#     print(name)
#     #array_range

# for names in range(0,2):
#     print(names)

    #function with for loop
def print_time(task_name):
        print('task competed!')
        print(task_name)
        print()
        print('time and date at exection of code :'+str( datetime.now()))
        print()

for x in range(0,10):
        print(x)
print_time('completed for loop')

    
