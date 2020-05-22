first_name='vinusha'
last_name='janga'
name=first_name +''+ last_name
print(name.upper())
print(name.lower())
print(name.capitalize())
#print(name.count(a))
print('Hello,' + first_name  +' '+ last_name)
#using Place-holders
output='Hello,{} {}'.format(  first_name  , last_name )
print(output)
output='Hello,{0} {1}'.format(  first_name  , last_name )
print(output)
output='Hello,{1} ,{0}'.format(  first_name  , last_name )
print(output)
output=f'Hello, { first_name.capitalize() } ,{last_name.capitalize() }'
print(output)