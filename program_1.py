#title:initials
#author: michael stoll
#date: 3/17/2025
first_name = str(input('Enter first name:'))
result1 = first_name.replace(first_name, first_name[0])
middle_name = str(input('Enter middle name:'))
result2 = middle_name.replace(middle_name, middle_name[0])
last_name = str(input('Enter last name:'))
result3 = last_name.replace(last_name, last_name[0])
print(result1 + '.' , result2 + '.', result3 + '.')