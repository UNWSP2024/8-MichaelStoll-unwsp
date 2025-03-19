#title:Course info
#author: michael stoll
#date: 3/17/2025
all_relevant_courses = []
number_of_courses = int(input('Input number of courses:'))
filter_subject = str(input('Filtered to the course subject:'))
for count in range(number_of_courses):
    course_info = [str(input('Course ID:'))] + [str(input('Course name:'))]
    if filter_subject in course_info[0]:
        all_relevant_courses.append(course_info)
print(all_relevant_courses)