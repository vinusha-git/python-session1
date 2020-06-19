# gpa=float(input('enter grade'))
# lowest_grade=float(input('enter the lowest grade'))
# if gpa>=.85 and lowest_grade>=.70:
#   print('well done')

#using boolean

gpa=float(input('enter grade'))
lowest_grade=float(input('enter the lowest grade'))
if gpa>=.85 and lowest_grade>=.70:
   comment=True
else:
    comment=False
if comment:
    print('well done')