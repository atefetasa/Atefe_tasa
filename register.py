import csv
import json
import os
import file_handler
import logging
logging.basicConfig(filename='logfile.log',filemode='w',level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(message)s')


courses=[]
students_log_in_information=[]
students_information=[]
education_responsible_information=[]

execute_counter_1=0
execute_counter_2=0
execute_counter_3=0


def course_registration(course_name, teacher_name, unit, capacity, course_group):
    global execute_counter_1
    if execute_counter_1 == 0:
        with open('courses.json','r') as file:
            data = json.load(file)
            if data:
                logging.info("file was not empty")
                for dictionary in data:
                    courses.append(dictionary)
    with open('courses.json','w') as courses_file:
        course_dict={'course_name':course_name,'teacher_name':teacher_name,'unit':unit,
                     'capacity':capacity,'course_group':course_group}
        courses.append(course_dict)
        json.dump(courses,courses_file)
    execute_counter_1 += 1
    print(f"{course_name} course has been successfully added to the courses.")
    logging.info(f"{course_name} course has been successfully added to the courses.")


def student_registration(first_name,last_name,student_code,national_code,major):
    global execute_counter_2
    if execute_counter_2 == 0:
        with open('StudentsLog_In_file.json', 'r') as file:
            data = json.load(file)
            if data:
                logging.info("file was not empty!")
                for dictionary in data:
                    students_log_in_information.append(dictionary)
    with open('StudentsLog_In_file.json', 'w') as file:
        student_log_in_dict = {'user_name':national_code, 'password':student_code ,'locked':0}
        students_log_in_information.append(student_log_in_dict)
        json.dump(students_log_in_information, file)
    if execute_counter_2 == 0:
        with open('students.json', 'r') as file:
            data = json.load(file)
            if data:
                for dictionary in data:
                    students_information.append(dictionary)
    with open('students.json', 'w') as students_file:
        student_information_dict = {'first_name': first_name, 'last_name': last_name, 'student_code': student_code,
                                    'national_code':national_code,'major': major}
        students_information.append(student_information_dict)
        json.dump(students_information, students_file)
    execute_counter_2+=1
    print(" Welcome !you have been successfully registered")
    logging.info("Welcome !you have been successfully registered")


def education_resp_registration(user_name,password):
    global execute_counter_3
    if execute_counter_3 == 0:
        with open('EducationR_Log_In_file.json','r') as file:
            data=json.load(file)
            if data:
                logging.info("file was not empty")
                for dictionary in data:
                    education_responsible_information.append(dictionary)
    with open('EducationR_Log_In_file.json','w') as e_file:
        e_log_in_dict={'user_name':user_name,'password':password ,'locked':0}
        education_responsible_information.append(e_log_in_dict)
        json.dump(education_responsible_information,e_file)
    execute_counter_3+=1
    print("\n Welcome !you have been successfully registered")
    logging.info("Welcome !you have been successfully registered")


def student_log_in(password):
    record_find = 0
    record_locked = 0
    with open('StudentsLog_In_file.json', 'r') as students_file:
        data=json.load(students_file)
        for dictionary in data:
            if dictionary['password'] == password:
                record_find = 1
                logging.info(f"user with password {password} has a record in system.")
                if dictionary['locked'] == 0:
                    logging.info(f"user with password {password} is not locked.")
                    break
                elif dictionary['locked'] == 1:
                    logging.info(f"user with password {password} is locked.")
                    record_locked = 1
        return record_find,record_locked


def education_resp_log_in(password):
    record_find = 0
    record_locked = 0
    with open('EducationR_Log_In_file.json', 'r') as file:
        data = json.load(file)
        for dictionary in data:
            if dictionary['password'] == password:
                logging.info(f"user with password {password} has a record in system.")
                record_find = 1
                if dictionary['locked'] == 0:
                    logging.info(f"user with password {password} is not locked.")
                    break
                elif dictionary['locked'] == 1:
                    logging.info(f"user with password {password} is locked.")
                    record_locked = 1
        return record_find, record_locked


def lock_acount(file_name,user_name):
    accounts_information_list = []
    account=file_handler.search_in_file(file_name,'user_name',user_name)
    account_dictionary=account[0]
    with open(file_name,'r') as file:
        data=json.load(file)
        for dictionary in data:
            accounts_information_list.append(dictionary)
    for item in accounts_information_list:
        if account_dictionary == item:
            item['locked'] = 1
    with open(file_name,'w') as myfile:
        json.dump(accounts_information_list,myfile)
    print("your account has been locked.")
    logging.info(f"the account with {user_name} user name is locked.")


def password_validation(password):
    password=str(password)
    if len(password) == 9:
        logging.info(f"the {password} was true.")
        return True
    else:
        logging.error(f"the password {password} was not true.")
        return False


def check_entered_password(file_name,user_name,password):
    counter = 1
    while counter <= 3:
        validation = student_log_in(password)
        if validation[0] == 1 and validation[1] == 0:
            print("welcome!you have logged in.")
            logging.info(f"the user with {password} has been logged in.")
            break
        elif validation[0] == 1 and validation[1] == 1:
            print("you can not access to your account because it's locked")
            logging.warning(f"the user with {password} password can not access to his/her account because its locked.")
            break
        elif validation[0] == 0:
            if counter == 3:
                lock_acount(file_name, user_name)
                logging.info(f"he user with {password} password became locked")
                counter+=1
            else:
                print("your password is incorrect.")
                logging.warning("the user has entered the wrong password.")
                user_name = input("please re enter your user name:")
                password = input("please re enter your password:")
                counter += 1
    return password


def checking_education_responsible_national_code(national_code):
    national_codes_list=[]
    with open('Admins_nationalcodes.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            national_codes_list.append(list(row))
        for item in national_codes_list:
            for NationalCode in item:
                if NationalCode == national_code:
                    logging.info("admins national code had been found in the file")
                    return True





































