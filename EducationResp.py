import json
import logging
logging.basicConfig(filename='logfile.log',filemode='w',level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(message)s')


class EducationResponsible:
    def __init__(self,user_name,password):
        self.user_name=user_name
        self.password=password

    @staticmethod
    def choose_student(student_code):
        return f"with this method education responsible can choose a student " \
               f"by his student code and see which courses he/she had choosed .this method is a static method because " \
               f"it works with files not objects"

    @staticmethod
    def all_students_list():
        return f"this method only returns the names and student codes of students " \
               f"so education responsible can choose a student."
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


