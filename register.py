import csv
import hashlib
import json
import os
import file_handler
import logging
import time
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
        flag = 0
        course_dict={'course_name':course_name,'teacher_name':teacher_name,'unit':unit,
                     'capacity':capacity,'course_group':course_group}
        for dictionary in courses:
            if dictionary == course_dict:
                flag = 1
                print("this course exists in courses file you don't need to register it.")
                break
        if flag == 0:
            courses.append(course_dict)
        json.dump(courses, courses_file)
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
        flag = 0
        password=hashlib.sha224(student_code.encode())
        password=password.hexdigest()
        student_log_in_dict = {'user_name':national_code, 'password':password ,'locked':0}
        for student in students_log_in_information:
            if student['user_name'] == student_log_in_dict['user_name']:
                flag = 1
                print("you already have registered in system before you don't need to register again.")
                break
        if flag == 0:
            students_log_in_information.append(student_log_in_dict)
        json.dump(students_log_in_information, file)
    if flag == 0:
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
        return True
    elif flag == 1:
        return False


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
        flag = 0
        password=hashlib.sha224(password.encode())
        password=password.hexdigest()
        e_log_in_dict={'user_name':user_name,'password':password ,'locked':0}
        for dictionary in education_responsible_information:
            if dictionary['user_name'] == e_log_in_dict['user_name']:
                flag = 1
                print("you already have registered in system before you don't need to register again.")
                break
        if flag == 0:
            education_responsible_information.append(e_log_in_dict)
        json.dump(education_responsible_information, e_file)
        if flag == 0:
            print("\n Welcome !you have been successfully registered")
            logging.info("Welcome !you have been successfully registered")
            return True
        elif flag == 1:
            return False
    execute_counter_3+=1


def student_log_in(user_name,password):
    record_find = 0
    record_locked = 0
    user_name_find = 0
    password_find = 0
    password=hashlib.sha224(password.encode())
    password=password.hexdigest()
    with open('StudentsLog_In_file.json', 'r') as students_file:
        data=json.load(students_file)
        for dictionary in data:
            if dictionary['user_name'] == user_name:
                user_name_find = 1
            if dictionary['password'] == password:
                password_find = 1
            if user_name_find == 1 and password_find == 1:
                record_find = 1
                logging.info(f"user with password {password} password has a record in system.")
                if dictionary['locked'] == 0:
                    logging.info(f"user with password {password} password is not locked.")
                    break
                elif dictionary['locked'] == 1:
                    logging.info(f"user with password {password} password is locked.")
                    record_locked = 1
                    break
        return user_name_find,password_find,record_find,record_locked


def education_resp_log_in(user_name,password):
    record_find = 0
    record_locked = 0
    user_name_find = 0
    password_find = 0
    password = hashlib.sha224(password.encode())
    password = password.hexdigest()
    with open('EducationR_Log_In_file.json', 'r') as file:
        data = json.load(file)
        for dictionary in data:
            if dictionary['user_name'] == user_name:
                user_name_find = 1
            if dictionary['password'] == password:
                password_find = 1
            if user_name_find == 1 and password_find == 1:
                record_find = 1
                logging.info(f"user with password {password} password has a record in system.")
                if dictionary['locked'] == 0:
                    logging.info(f"user with password {password} password is not locked.")
                    break
                elif dictionary['locked'] == 1:
                    logging.info(f"user with password {password} password is locked.")
                    record_locked = 1
                    break
        return user_name_find, password_find, record_find, record_locked


def lock_acount(file_name,user_name=None,password=None):
    sec = 180
    if user_name:
        account=file_handler.search_in_file(file_name,'user_name',user_name)
        account_dictionary=account[0]
    elif password:
        account = file_handler.search_in_file(file_name, 'password', password)
        account_dictionary = account[0]
    with open(file_name,'r') as file:
        data=json.load(file)
    for dictionary in data:
        if account_dictionary == dictionary:
            dictionary['locked'] = 1
    with open(file_name,'w') as myfile:
        json.dump(data,myfile)
    print("your account has been locked.")
    logging.info(f"the account with {user_name} user name is locked.")
    time.sleep(sec)
    unlock_account(file_name,user_name,password)


def unlock_account(file_name,user_name=None,password=None):
    if user_name:
        account=file_handler.search_in_file(file_name,'user_name',user_name)
        account_dictionary=account[0]
    elif password:
        account = file_handler.search_in_file(file_name, 'password', password)
        account_dictionary = account[0]
    with open(file_name,'r') as file:
        data=json.load(file)
    for dictionary in data:
        if account_dictionary == dictionary:
            if dictionary['locked'] == 1:
                dictionary['locked'] = 0
    with open(file_name,'w') as myfile:
        json.dump(data,myfile)
    logging.info(f"the account is unlocked.")


def password_validation(password):
    password=str(password)
    if len(password) == 9:
        with open('EducationR_Log_In_file.json','r') as file:
            flag = 0
            data = json.load(file)
            for dictionary in data:
                if dictionary['password'] == password:
                    flag = 1
                    print("your chosen password has been picked by some one else.")
                    break
            if flag == 0:
                return True
            elif flag == 1:
                return False
    else:
        print("your password is not 9 digits.")
        logging.info("the password was not 9 digits.")
        return False


def check_entered_password(file_name,user_name,password):
    counter = 1
    while counter <= 3:
        if file_name == 'StudentsLog_In_file.json':
            validation = student_log_in(user_name,password)
        elif file_name == 'EducationR_Log_In_file.json':
            validation = education_resp_log_in(user_name, password)
        if validation[2] == 1 and validation[3] == 0:
            print("welcome!you have logged in.")
            logging.info(f"the user with {password} has been logged in.")
            break
        elif validation[2] == 1 and validation[3] == 1:
            print("you can not access to your account because it's locked")
            logging.warning(f"the user with {password} password can not access to his/her account because its locked.")
            break
        elif (validation[0] == 0 and validation[1] == 1) or (validation[0] == 1 and validation[1] == 0):
            if counter == 3:
                if validation[0] == 0 and validation[1] == 1:
                    lock_acount(file_name, password=password)
                    logging.info(f"he user with {password} password became locked")
                    counter+=1
                elif validation[0] == 1 and validation[1] == 0:
                    lock_acount(file_name, user_name=user_name)
                    logging.info("the user has became locked.")
                    counter += 1
            else:
                print("your user name or password is incorrect.")
                logging.warning("the user has entered the wrong password or user name.")
                user_name = input("please re enter your user name:")
                password = input("please re enter your password:")
                counter += 1
    return user_name,password


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








































