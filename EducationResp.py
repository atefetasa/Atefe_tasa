import json
import logging
import file_handler
logging.basicConfig(filename='logfile.log',filemode='w',level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(message)s')


class EducationResponsible:
    def __init__(self,user_name,password):
        self.user_name=user_name
        self.password=password

    @staticmethod
    def choose_student(student_code):
        student_choose_courses = 0
        student_exist = 0
        student=file_handler.search_in_file('students_courses.json','student_code',student_code)
        if student:
            dictionary=student[0]
            print(f"the number of units this student has taken:{dictionary['number_of_units']}")
            print("the list of course this student has taken:")
            for course in dictionary['courses_list']:
                print(course)
            student_exist = 1
            student_choose_courses = 1
        else:
            if file_handler.search_in_file('students.json','student_code',student_code):
                print("this student has not chosen any courses yet.")
                student_exist = 1
            else:
                print("there is no student with this student code in system.")
        return student_exist,student_choose_courses

    @staticmethod
    def all_students_list():
        with open('students.json','r') as file:
            data=json.load(file)
            for student in data:
                dictionary={'first_name':student['first_name'],
                            'last_name':student['last_name'],'student_code':student['student_code'],
                            'major':student['major']}
                print(dictionary)

    @classmethod
    def add_education_responsible(cls,user_name,password):
        logging.info("the education responsible object has been created.")
        return cls(user_name=user_name,password=password)

    @staticmethod
    def confirm_student_all_courses(student_code):
        with open('students_courses.json','r') as file:
            data=json.load(file)
            for dictionary in data:
                if dictionary['student_code'] == student_code:
                    for course in dictionary['courses_list']:
                        course['course_confirm'] = '1'
        print(f"all courses of student with {student_code} student code has been confirmed.")
        logging.info(f"all courses of student with {student_code} student code has been confirmed.")

    @staticmethod
    def reject_student_course(student_code,course_name):
        with open('students_courses.json','r') as file:
            data=json.load(file)
            for dictionary in data:
                if dictionary['student_code'] == student_code:
                    for course in dictionary['courses_list']:
                        if course['course_name'] == course_name:
                            course['course_confirm'] = '0'
        print(f"the {course_name} rejection for {student_code} student was successfull.")
        logging.info(f"the {course_name} rejection for {student_code} student was successfull.")


