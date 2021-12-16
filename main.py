import json

import file_handler
import register
import student
import EducationResp
import course
import logging
logging.basicConfig(filename='logfile.log',filemode='w',level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(message)s')

# register.course_registration('computer architeture','bahrai',4,25,'software engineering')
# register.course_registration('basis economies','farrokh',3,30,'economics')
# register.course_registration('water management','sadr',2,25,'management')
# register.course_registration('algorithem','izadkhah',4,25,'software engineering')
# register.course_registration('operating systems','lotfi',3,30,'software engineering')
# register.course_registration('mechanics of materials','borhani',3,22,'civil engineering')

log_in = input("do you have an account?\n 1)I don't have account (sign up)\n 2)I have an account (log in)\n")
if log_in == '1':
    user_input1 = input("are you a student or education responsible?\n 1)student\n 2)Education Responsible\n")
    if user_input1 == '1':
        first_name = input("please enter your first name:")
        last_name = input("please enter your last name:")
        student_code = input("please enter your student code:")
        national_code=input("please enter your national code:")
        major = input("please enter your major:")
        user_name = national_code
        password = student_code
        register.student_registration(first_name, last_name, student_code,national_code, major)
        print("\n")
        print(f"please attention \n your user name is your national code: {user_name}\n your password is your student code:"
              f"{password}")
        logging.info(f"the user name and password was shown to the user with {password} password.")
        new_student=student.Student.add_student(first_name,last_name,student_code,national_code,major)
        courses_list=new_student.show_choosable_courses()
        print("you can choose these courses:")
        for course in courses_list:
            print(f"{course}\n")
        logging.info("the courses had been shown to the student.")
    elif user_input1 == '2':
        user_name = input("please enter your national code:")
        if register.checking_education_responsible_national_code(user_name):
            while True:
                try:
                    password = input("please enter a 9 digit number as password:")
                    validation = register.password_validation(password)
                    if validation:
                        break
                    else:
                        logging.error(f"the password {password} was invalid.")
                        raise ValueError('this password is invalid')
                except ValueError as e:
                    print(e)
            education_resp1=EducationResp.EducationResponsible.add_education_responsible(user_name,password)
            register.education_resp_registration(user_name,password)
            print("\n")
            print(f"please attention \n your user name is your national code: {user_name}\n your password is:"
                  f"{password}")
            logging.info(f"the user name and password was shown to the user with {password} password.")

            user_input2=input("what do you want to do:\n 1)define a new course\n 2)see the list of students \n")
            if user_input2 == '1':
                course_name=input("enter the course name:")
                teacher_name=input("enter the teacher name:")
                unit=input("enter course number of units:")
                capacity=input("enter the course capacity:")
                course_group=input("enter the course group:")
                register.course_registration(course_name,teacher_name,unit,capacity,course_group)
                course1=course.Course.add_course(course_name,teacher_name,unit,capacity,course_group)
            elif user_input2 == '2':
                EducationResp.EducationResponsible.all_students_list()
                user_input3=input("which one of these students do you want to choose\n "
                                  "to see more information about him/her?\n"
                                  "please enter his/her student code:")
                EducationResp.EducationResponsible.choose_student(user_input3)
                user_input4=input("do you confirm all his/her courses or not?\n 1)Yes\n 2)No")
                if user_input4 == '1':
                    EducationResp.EducationResponsible.confirm_student_all_courses(user_input3)
                elif user_input4 == '2':
                    while True:
                        user_input5=str(input("please enter the course name you want to reject:"))
                        EducationResp.EducationResponsible.reject_student_course(user_input3,user_input5)
                        user_input6=input("do you want to reject another course?\n 1)Yes \n 2)No")
                        if user_input6 == '2':
                            break
        else:
            print("you have not the permission to register as education responsible \n"
                  "because your national code has not been registered as admin in system.")
            logging.warning(f"the user with {user_name} national code is not allowed to access to the system as admin. ")
elif log_in == '2':
    user_name=input("please enter your user name:")
    password=input("please enter your password:")
    user_input1 = input("are you a student or education responsible?\n 1)student\n 2)Education Responsible\n")
    if user_input1 == '1':
        new_password=register.check_entered_password('StudentsLog_In_file.json',user_name,password)
        status_tuple=register.student_log_in(new_password)
        if status_tuple[0] == 1 and status_tuple[1] == 0:
            student_information=file_handler.search_in_file('students.json','student_code',str(password))
            student_dictionary=student_information[0]
            new_student=student.Student.add_student(student_dictionary['first_name'],student_dictionary['last_name'],
                                        student_dictionary['student_code'],student_dictionary['national_code'],student_dictionary['major'])
            courses_list = new_student.show_choosable_courses()
            print("you can choose these courses:")
            for course in courses_list:
                print(f"{course}\n")
            print('\n')
            course_name=str(input("Enter the course name you want to choose:"))
            new_student.select_units(course_name)






































