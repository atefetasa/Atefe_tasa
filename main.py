import json

import file_handler
import register
import student
import EducationResp
import course
import log



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
        national_code = input("please enter your national code:")
        major = input("please enter your major:")
        user_name = national_code
        password = student_code
        registration_validation = register.student_registration(first_name, last_name, student_code, national_code,
                                                                major)
        if registration_validation:
            print("\n")
            print(
                f"please attention \n your user name is your national code: {user_name}\n "
                f"your password is your student code:{password}\n")
            new_student = student.Student.add_student(first_name, last_name, student_code, national_code, major)
            courses_list = new_student.show_choosable_courses()
            if courses_list:
                print("you can choose these courses:")
                for course in courses_list:
                    print(f"{course}\n")
                print('\n')
            else:
                print("we have no courses for your major to show you.")
            while True:
                course_name = str(input("Enter the course name you want to choose:"))
                result=new_student.prevent_duplicate_courses_in_unit_selection(course_name)
                if result:
                    new_student=new_student.select_units(course_name)
                    new_student.show_chosen_courses()
                    user_input_2=input("\ndo you want to do the final register?\n 1)Yes\n 2)No")
                    if user_input_2 == '1':
                        result_2=new_student.final_unit_selection_registration()
                        if result_2:
                            print("your selected units has been successfully registered.")
                            break
                else:
                    print("you can not select one course two times.")
    elif user_input1 == '2':
        user_name = input("please enter your national code:")
        if register.checking_education_responsible_national_code(user_name):
            while True:
                password = input("please enter a 9 digit number as password:")
                validation = register.password_validation(password)
                if validation:
                    break
                else:
                    log.warning_logger.error(f"education reponsible's  password was invalid.")
            education_resp1 = EducationResp.EducationResponsible.add_education_responsible(user_name, password)
            registration_validation = register.education_resp_registration(user_name, password)
            if registration_validation:
                print("\n")
                print(f"please attention \n your user name is your national code: {user_name}\n your password is:"
                      f"{password}\n")

                user_input2 = input("what do you want to do:\n 1)define a new course\n 2)see the list of students \n")
                if user_input2 == '1':
                    course_name = input("enter the course name:")
                    teacher_name = input("enter the teacher name:")
                    unit = input("enter course number of units:")
                    capacity = input("enter the course capacity:")
                    course_group = input("enter the course group:")
                    register.course_registration(course_name, teacher_name, unit, capacity, course_group)
                    course1 = course.Course.add_course(course_name, teacher_name, unit, capacity, course_group)
                elif user_input2 == '2':
                    EducationResp.EducationResponsible.all_students_list()
                    while True:
                        user_input3 = input("\nwhich one of these students do you want to choose\n "
                                            "to see his/her selected courses?\n"
                                            "please enter his/her student code:")
                        student_status=EducationResp.EducationResponsible.choose_student(user_input3)
                        if student_status[0] == 1 and student_status[1] == 1:
                            user_input4 = input("do you confirm all his/her courses or not?\n 1)Yes\n 2)No")
                            if user_input4 == '1':
                                EducationResp.EducationResponsible.confirm_student_all_courses(user_input3)
                            elif user_input4 == '2':
                                while True:
                                    user_input5 = str(input("please enter the course name you want to reject:"))
                                    EducationResp.EducationResponsible.reject_student_course(user_input3, user_input5)
                                    user_input6 = input("do you want to reject another course?\n 1)Yes \n 2)No")
                                    if user_input6 == '2':
                                        break
                                break
                        elif student_status[0] == 1 and student_status[1] == 0:
                            print("\nthis student has not selected any units yet.")
                            break
                        elif student_status[0] == 0 and student_status[1] == 0:
                            print("\nyou have entered an incorrect student code this student code doesn't exist")
        else:
            print("you have not the permission to register as education responsible \n"
                  "because your national code has not been registered as admin in system.")
            log.warning_logger.warning(
                f"the user with {user_name} national code is not allowed to access to the system as admin. ")
elif log_in == '2':
    user_name = input("please enter your user name:")
    password = input("please enter your password:")
    user_input1 = input("are you a student or education responsible?\n 1)student\n 2)Education Responsible\n")
    if user_input1 == '1':
        new_password_and_user_name = register.check_entered_password('StudentsLog_In_file.json', user_name, password)
        status_tuple = register.student_log_in(new_password_and_user_name[0], new_password_and_user_name[1])
        if status_tuple[2] == 1 and status_tuple[3] == 0:
            student_information = file_handler.search_in_file('students.json', 'student_code'
                                                              , new_password_and_user_name[1])
            student_dictionary = student_information[0]
            new_student = student.Student.add_student(student_dictionary['first_name'], student_dictionary['last_name'],
                                                      student_dictionary['student_code'],
                                                      student_dictionary['national_code'], student_dictionary['major'])
            courses_list = new_student.show_choosable_courses()
            if courses_list:
                print("you can choose these courses:")
                for course in courses_list:
                    print(f"{course}\n")
                print('\n')
            else:
                print("we have no courses for your major to show you.")
            while True:
                course_name = str(input("Enter the course name you want to choose:"))
                result=new_student.prevent_duplicate_courses_in_unit_selection(course_name)
                if result:
                    new_student=new_student.select_units(course_name)
                    new_student.show_chosen_courses()
                    user_input_2=input("\ndo you want to do the final register?\n 1)Yes\n 2)No")
                    if user_input_2 == '1':
                        result_2=new_student.final_unit_selection_registration()
                        if result_2:
                            print("your selected units has been successfully registered.")
                            break
                else:
                    print("you can not select one course two times.")
    elif user_input1 == '2':
        new_password_and_user_name = register.check_entered_password('EducationR_Log_In_file.json', user_name, password)
        status_tuple = register.education_resp_log_in(new_password_and_user_name[0], new_password_and_user_name[1])
        if status_tuple[2] == 1 and status_tuple[3] == 0:
            education_resp1 = EducationResp.EducationResponsible.add_education_responsible(new_password_and_user_name[0]
                                                                                           , new_password_and_user_name[1])
            user_input2 = input("what do you want to do?\n1)define a new course\n2)see the list of students\n")
            if user_input2 == '1':
                course_name = input("enter the course name:")
                teacher_name = input("enter the teacher name:")
                unit = input("enter course number of units:")
                capacity = input("enter the course capacity:")
                course_group = input("enter the course group:")
                register.course_registration(course_name, teacher_name, unit, capacity, course_group)
                course1 = course.Course.add_course(course_name, teacher_name, unit, capacity, course_group)
            elif user_input2 == '2':
                EducationResp.EducationResponsible.all_students_list()
                while True:
                    user_input3 = input("\nwhich one of these students do you want to choose\n "
                                        "to see his/her selected courses?\n"
                                        "please enter his/her student code:")
                    student_status=EducationResp.EducationResponsible.choose_student(user_input3)
                    if student_status[0] == 1 and student_status[1] == 1:
                        user_input4 = input("do you confirm all his/her courses or not?\n 1)Yes\n 2)No")
                        if user_input4 == '1':
                            EducationResp.EducationResponsible.confirm_student_all_courses(user_input3)
                            break
                        elif user_input4 == '2':
                            while True:
                                user_input5 = str(input("please enter the course name you want to reject:"))
                                EducationResp.EducationResponsible.reject_student_course(user_input3, user_input5)
                                user_input6 = input("do you want to reject another course?\n 1)Yes \n 2)No")
                                if user_input6 == '2':
                                    break
                            break
                    elif student_status[0] == 1 and student_status[1] == 0:
                        print("\nthis student has not selected any units yet.")
                        break
                    elif student_status[0] == 0 and student_status[1] == 0:
                        print("\nyou have entered an incorrect student code this student code doesn't exist")





