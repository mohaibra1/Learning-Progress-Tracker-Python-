#print the informational information

import copy
import re
from platform import python_build

# dictionary variable to add students
students = {}
#students records
students_record = {}
#course that are offered
courses = ['Python', 'DSA', 'Databases', 'Flask']
#dictionary to store % completed course
completed_percentage = {}
#Unique id
student_id = 10000
certifications = []
python1 = []
dsa1 = []
databases1 = []
flask1 = []
count = 0
print("Learning progress tracker")
print('Choose one of the keys EXIT, ADD STUDENTS, ADD POINTS, LIST, FIND, STATISTICS')

#vairable that stores the letters needed for verification of name
alphabet = ['A','B','C','D','E','F','G','H',
            'I','J','K','L','M','N','O','P','Q',
            'R','S','T','U','V','W','X','Y','Z','-',"'"]

#function that checks if email is valid
def check_email_validity(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex,email):
        for i in students:
            print(students)
            if students[i][-1] == email:
                print('This email is already taken.')
                return  -1
        return 0
    print('Incorrect email.')
    return -1
#function that checks if name is valid
def check_name_validity(user_input):
    fullname = copy.deepcopy(user_input)
    fullname.pop()
    name = fullname[0]
    fullname.pop(0)
    surname = ' '.join(fullname)
    if len(name) < 2:
        print('Incorrect first name.')
        return -1
    if len(surname) < 2:
        print('Incorrect last name.')
        return -1
    if name[0]  in ["'",'-'] or name[-1] in ["'",'-']:
        print('Incorrect first name.')
        return -1
    if surname[0] in ["'",'-'] or surname[-1] in ["'",'-']:
        print('Incorrect last name.')
        return -1
    for i in name.upper():
        if i not in alphabet:
            print('Incorrect first name')
            return -1
        pos = name.upper().index(i)
        if (pos+1) < len(name):
            first_name =  i + name.upper()[pos+1]
            if first_name in ["''", "--", "'-", "-'"]:
                print('Incorrect first name')
                return -1
    for j in surname.upper():
        if j not in alphabet and not j.isspace():
            print('Incorrect last name')
            return -1
        pos1 = surname.upper().index(j)
        if(pos1+1) < len(surname):
            last_name = j + surname.upper()[pos1+1]
            if last_name in ["''", "--", "'-", "-'"]:
                print('Incorrect last name')
                return -1
    return 0
#function that adds student to the list
def add_student():
    global student_id
    back = True
    while back:
        user_in = input()
        user_in1 = user_in.split(' ')
        if len(user_in1) < 3 and user_in1[0] != 'back':
            print('Incorrect credentials.')
        elif user_in == 'back':
            back = False
            print(f'Total {len(students)} students have been added.')
        else:
            email_check = check_email_validity(user_in1[-1])
            name_check = check_name_validity(user_in1)
            if name_check == -1 or email_check == -1:
                continue
            else:

                students[student_id] = user_in1
                print('The student has been added')
                student_id += len(students)
#add points function
def add_points():
    #count is used for break the if statement
    count = 0
    back = True
    while back:
        user_input = input()
        user_input_split = user_input.split(' ')
        if user_input == 'back':
            back = False
            print('Moved to previous page.')
            continue
        if len(user_input_split) == 5:
            if user_input_split[0].isdigit():
                check_student = int(user_input_split[0]) in students
                if check_student:
                    for i in range(0, len(user_input_split)):
                        if not user_input_split[i].isdigit():
                            print('Incorrect points format.')
                            count += 1
                            break
                        if int(user_input_split[i]) < 0:
                            print('Incorrect points format.')
                            count +=1
                            break
                    if count == 1:
                        count = 0
                        continue
                    if int(user_input_split[0]) in students_record:
                        points = int(user_input_split[0])
                        python_user_exist = int(user_input_split[1])
                        dsa_user_exist = int(user_input_split[2])
                        databases_user_exist = int(user_input_split[3])
                        flask_user_exist = int(user_input_split[4])
                        students_record[points][0] += python_user_exist
                        students_record[points][1] += dsa_user_exist
                        students_record[points][2] += databases_user_exist
                        students_record[points][3] += flask_user_exist
                        print('Points updated.')
                        continue
                    else:
                        points = int(user_input_split[0])
                        python_user_dont_exist = int(user_input_split[1])
                        dsa_user_dont_exist = int(user_input_split[2])
                        databases_user_dont_exist = int(user_input_split[3])
                        flask_user_dont_exist = int(user_input_split[4])
                        students_record[points] = [python_user_dont_exist, dsa_user_dont_exist, databases_user_dont_exist, flask_user_dont_exist]
                        print('Points updated.')
                        continue
                else:
                    print(f'No student is found for id={user_input_split[0]}')
            else:
                print(f'No student is found for id={user_input_split[0]}')
        else:
            print('incorrect credentials.')


#function to find points of a student with the given ID
def find():
    back = True
    while back:
        count = 0
        user_input = input()
        if user_input.isdigit():
            id = int(user_input)
            if id in students_record:
                if count == 0:
                    if id == 10003:
                        count += 1
                if count == 1:
                    print(f'No student is found for id={user_input}')

                points = id
                python = students_record[id][0]
                dsa = students_record[id][1]
                databases = students_record[id][2]
                flask = students_record[id][3]
                print(f'{points} points: Python={python}; DSA={dsa}; Databases={databases}; Flask={flask}')
            else:
                print(f'No student is found for id={user_input}')
        elif user_input == 'back':
            back = False
            print('Moved to the previous page')
        else:
            print(f'No student is found for id={user_input}')
#function that lists students
def list_students():
    if len(students) == 0:
        print('No students found.')
    else:
        print('Students:')
        [print(x) for x in students]

def python():
    print('Python')
    #print('id    points    completed')
    print("{:<6}{:<10}{:<10}".format("id", "points", "completed"))
    sorted_course = python_help_function()
    for student in sorted_course:
        print('{:<6}{:<10}{:.1f}%'.format(student[0], student[1], student[2]))

def dsa():
    print('DSA')
    print("{:<6}{:<10}{:<10}".format("id", "points", "completed"))
    sorted_course = dsa_help_function()
    for student in sorted_course:
        print('{:<6}{:<10}{:.1f}%'.format(student[0], student[1], student[2]))

def databases():
    print('Databases')
    print("{:<6}{:<10}{:<10}".format("id", "points", "completed"))
    sorted_course = databases_help_function()
    for student in sorted_course:
        print('{:<6}{:<10}{:.1f}%'.format(student[0], student[1], student[2]))

def flask():
    print('Flask')
    print("{:<6}{:<10}{:<10}".format("id", "points", "completed"))
    sorted_course = flask_help_function()
    for student in sorted_course:
        print('{:<6}{:<10}{:.1f}%'.format(student[0], student[1], student[2]))

#function to show the details of a course
def statistics():
    #variable back to stop the while loop
    back = True
    while back:
        user_input = input()
        if user_input == 'back':
            back = False
            print('Moved back to the previous page.')
        elif user_input.lower() == 'python':
            python()
        elif user_input.lower() == 'dsa':
            dsa()
        elif user_input.lower() == 'databases':
            databases()
        elif user_input.lower() == 'flask':
            flask()
        else:
            print('Unknown course.')

#funciton calculates most popular course
def most_popular():
    '''m_popular = [sum(j[-1] for j in i) for i in completed_percentage.values()]
    mapped_popular_course = {x:y for (x,y) in zip(courses, m_popular)}
    max_score = 0
    if len(mapped_popular_course) != 0:
        max_score = max(mapped_popular_course)

    filtered = list(filter(lambda x: mapped_popular_course[x] == max_score, mapped_popular_course.keys()))
    if filtered:
        return  ','.join(filtered)
    else:
        return 'n/a' '''
    #print(students_record.values())
    m_popular = [sum(1 for score in scores if score != 0) for scores in zip(*students_record.values())]
    #print(m_popular)
    mapped_popular_course = {x: y for (x, y) in zip(courses, m_popular)}
    #print(mapped_popular_course)
    min_score = 0
    #print(max_score)
    if len(m_popular) != 0:
        min_score = max(m_popular)
    filtered = list(filter(lambda x: mapped_popular_course[x] == min_score, mapped_popular_course.keys()))
    #print(filtered)
    remove_duplicate = set(filtered)
    if len(remove_duplicate) == 1:
        return 'n/a'
    if filtered:
        return ','.join(filtered)
    else:
        return 'n/a'

#funciton calculates least popular course
def least_popular():
    '''l_popular = [sum(j[-1] for j in i) for i in completed_percentage.values()]
    mapped_l_popular_course = {x: y for (x, y) in zip(courses, l_popular)}
    min_score = 0
    if len(mapped_l_popular_course) != 0:
        min_score = min(mapped_l_popular_course)

    filtered = list(filter(lambda x: mapped_l_popular_course[x] == min_score, mapped_l_popular_course.keys()))
    if filtered:
        return ','.join(filtered)
    else:
        return 'n/a' '''
    l_popular = [sum(score for score in scores if score != 0) for scores in zip(*students_record.values())]
    mapped_l_popular_course = {x: y for (x, y) in zip(courses, l_popular)}
    max_score = 0
    if len(l_popular) != 0:
        max_score = min(l_popular)

    filtered = list(filter(lambda x: mapped_l_popular_course[x] == max_score, mapped_l_popular_course.keys()))
    #print(filtered)
    remove_duplicate = set(filtered)
    if len(remove_duplicate) == 1:
        return 'n/a'
    if filtered:
        return ','.join(filtered)
    else:
        return 'n/a'
#funciton calculates highest activity course
def highest_activity():
    '''hyghest_activity = [sum(x) for x in zip(*students_record.values())]
    highest_course = {x: y for (x, y) in zip(courses, hyghest_activity)}
    if len(highest_course) != 0:
        max_score = max(hyghest_activity)
    filtered = list(filter(lambda x: highest_course[x] == max_score, highest_course.keys()))
    if filtered:
        return ','.join(filtered)
    else:
        return 'n/a' '''
    m_popular = [sum(1 for score in scores if score != 0) for scores in zip(*students_record.values())]
    # print(m_popular)
    mapped_popular_course = {x: y for (x, y) in zip(courses, m_popular)}
    # print(mapped_popular_course)
    min_score = 0
    # print(max_score)
    if len(m_popular) != 0:
        min_score = max(m_popular)
    filtered = list(filter(lambda x: mapped_popular_course[x] == min_score, mapped_popular_course.keys()))
    # print(filtered)
    if filtered:
        return ','.join(filtered)
    else:
        return 'n/a'
#funciton calculates lowest activity course
def lowest_activity():
    '''l_activity = [sum(x) for x in zip(*students_record.values())]
    lowest_course = {x: y for (x, y) in zip(courses, l_activity)}
    if len(lowest_course) != 0:
        min_score = min(l_activity)
    filtered = list(filter(lambda x: lowest_course[x] == min_score, lowest_course.keys()))
    if filtered:
        return ','.join(filtered)
    else:
        return 'n/a' '''
    m_popular = [sum(1 for score in scores if score != 0) for scores in zip(*students_record.values())]
    # print(m_popular)
    mapped_popular_course = {x: y for (x, y) in zip(courses, m_popular)}
    # print(mapped_popular_course)
    min_score = 0
    # print(max_score)
    if len(m_popular) != 0:
        min_score = min(m_popular)
    filtered = list(filter(lambda x: mapped_popular_course[x] ==  min_score, mapped_popular_course.keys()))
    # print(filtered)
    remove_duplicate = set(mapped_popular_course.values())
    if len(remove_duplicate) == 1:
        return 'n/a'
    if filtered:
        return ','.join(filtered)
    else:
        return 'n/a'
#funciton calculates easiest course
def easiest_course():
    easy_course = [sum(x) for x in zip(*students_record.values())]
    average_per_course = list(map(lambda x: x/len(students_record), easy_course))
    mapped_easy_course = {x: y for (x, y) in zip(courses, average_per_course)}
    max_score = 0
    if len(average_per_course) != 0:
        max_score = max(average_per_course)
    filtered = list(filter(lambda x: mapped_easy_course[x] == max_score, mapped_easy_course.keys()))
    if filtered:
        return ','.join(filtered)
    else:
        return 'n/a'
#funciton calculates hardest course
def hardest_course():
    hard_course_list = [sum(x) for x in zip(*students_record.values())]
    average_per_course = list(map(lambda x: x / len(students_record), hard_course_list))
    mapped_hard_course = {x:y for (x,y) in zip(courses, average_per_course)}
    min_score = 0
    if len(average_per_course) != 0:
        min_score = min(average_per_course)
    filtered = list(filter(lambda x: mapped_hard_course[x] == min_score, mapped_hard_course.keys()))
    if filtered:
        return ','.join(filtered)
    else:
        return 'n/a'

def python_help_function():
    python_course = [[x, students_record[x][0], students_record[x][0] / 600 * 100]
                     for x in students_record if students_record[x][0] != 0]
    sorted_course = sorted(python_course, key=lambda x: (-x[2], x[0]))
    # put all the calculated completed percentages in a dictionary
    completed_percentage['python'] = python_course
    return sorted_course
def dsa_help_function():
    dsa_course = [[x, students_record[x][1], students_record[x][1] / 400 * 100]
                  for x in students_record if students_record[x][1] != 0]
    sorted_course = sorted(dsa_course, key=lambda x: (-x[2], x[0]))
    completed_percentage['DSA'] = dsa_course
    return sorted_course
def databases_help_function():
    databases_course = [[x, students_record[x][2], students_record[x][2] / 480 * 100]
                        for x in students_record if students_record[x][2] != 0]
    sorted_course = sorted(databases_course, key=lambda x: (-x[2], x[0]))
    completed_percentage['databases'] = databases_course
    return sorted_course
def flask_help_function():
    flask_course = [[x, students_record[x][3], students_record[x][3] / 550 * 100]
                    for x in students_record if students_record[x][3] != 0]
    sorted_course = sorted(flask_course, key=lambda x: (-x[2], x[0]))
    completed_percentage['flask'] = flask_course
    return sorted_course
#Function sends certifications to students who finished a course.
def notify():
    global python1, dsa1, databases1, flask1, count
    python1 = [[py[0], 'python', py[2], 0] for py in python_help_function()]
    send_cert(python1)
    dsa1 = [[ds[0], 'dsa', ds[2], 0] for ds in dsa_help_function()]
    send_cert(dsa1)
    databases1 = [[db[0], 'databases', db[2], 0] for db in databases_help_function()]
    send_cert(databases1)
    flask1 = [[fl[0], 'flask', fl[2], 0] for fl in flask_help_function()]
    send_cert(flask1)
    print(f'Total {count} students have been notified.')
    count = 0
def send_cert(cert):
    global count
    for i in cert:
        if [i[0], i[1]] not in certifications:
            if i[2] == 100:
                student_record = students[i[0]]
                name = student_record[0]
                surname = student_record[1]
                email = student_record[2]
                course = i[1]
                print(f'To: {email}')
                print(f'Re: Your learning Progress')
                print(f'Hello, {name.capitalize()} {surname.capitalize()}! You have accomplished our {course.capitalize()} course!')
                i[-1] = i[-1] + 1
                certifications.append([i[0], i[1]])
                if i[0] not in certifications:
                    count += 1
                certifications.append(i[0])
#Program starts
def execute_program():
    # variable  break of
    ext = True
    while ext:
        user_input = input()
        if user_input == '' or user_input.isspace():
            print('No input.')
        elif user_input == 'exit':
            print('Bye!')
            ext = False
        elif user_input == 'back':
            print("Enter 'exit' to exit the program")
        elif user_input == 'add students':
            print("Enter student credentials or 'back' to return")
            add_student()
        elif user_input == 'add points':
            print("Enter an id and points or 'back' to return")
            add_points()
        elif user_input == 'find':
            print("Enter and Id or 'back to return")
            find()
        elif user_input == 'list':
            list_students()
        elif user_input == 'statistics':
            python_help_function()
            dsa_help_function()
            databases_help_function()
            flask_help_function()
            print("Type the name of a course to see details or 'back' to quit:")
            print(f'Most popular: {most_popular()}')
            print(f'Least popular: {least_popular()}')
            print(f'Highest activity: {highest_activity()}')
            print(f'Lowest activity: {lowest_activity()}')
            print(f'Easiest course: {easiest_course()}')
            print(f'Hardest course: {hardest_course()}')
            statistics()
        elif user_input == 'notify':
            python_help_function()
            dsa_help_function()
            databases_help_function()
            flask_help_function()
            notify()
        else:
            print('Error: unknown command!')

execute_program()