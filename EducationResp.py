import json
import log
import file_handler


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
            try:
                dictionary=student[0]
                print(f"the number of units this student has taken:{dictionary['number_of_units']}")
                print("the list of course this student has taken:")
                for course in dictionary['courses_list']:
                    print(course)
                student_exist = 1
                student_choose_courses = 1
            except Exception as e:
                print(e)
                log.warning_logger.error(e)
        else:
            try:
                if file_handler.search_in_file('students.json','student_code',student_code):
                    print("this student has not chosen any courses yet.")
                    student_exist = 1
                else:
                    raise ValueError("there is no student with this student code in system.")
            except Exception as e:
                print(e)
                log.warning_logger.error(e)
        return student_exist,student_choose_courses

    @staticmethod
    def all_students_list():
        try:
            with open('students.json','r') as file:
                data=json.load(file)
                for student in data:
                    dictionary={'first_name':student['first_name'],
                                'last_name':student['last_name'],'student_code':student['student_code'],
                                'major':student['major']}
                    print(dictionary)
        except Exception as e:
            print(e)
            log.warning_logger.error(e)

    @classmethod
    def add_education_responsible(cls,user_name,password):
        return cls(user_name=user_name,password=password)

    @staticmethod
    def confirm_student_all_courses(student_code):
        try:
            with open('students_courses.json','r') as file:
                data=json.load(file)
                for dictionary in data:
                    if dictionary['student_code'] == student_code:
                        for course in dictionary['courses_list']:
                            course['course_confirm'] = '1'
        except Exception as e:
            print(e)
            log.warning_logger.error(e)
        try:
            with open('students_courses.json','w') as file:
                json.dump(data,file)
        except Exception as e:
            print(e)
            log.warning_logger.error(e)
        print(f"all courses of student with {student_code} student code has been confirmed.")
        log.info_logger.info(f"all courses of student with {student_code} student code has been confirmed."
                             ,exc_info=True)

    @staticmethod
    def reject_student_course(student_code,course_name):
        try:
            with open('students_courses.json','r') as file:
                data=json.load(file)
                for dictionary in data:
                    if dictionary['student_code'] == student_code:
                        for course in dictionary['courses_list']:
                            if course['course_name'] == course_name:
                                course['course_confirm'] = '0'
        except Exception as e:
            print(e)
            log.warning_logger.error(e)
        with open('students_courses.json','w') as file:
            json.dump(data,file)
        print(f"the {course_name} rejection for {student_code} student was successfull.")
        log.info_logger.info(f"the {course_name} rejection for {student_code} student was successfully.",exc_info=True)

