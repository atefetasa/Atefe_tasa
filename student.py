import json
import logging
import course
import file_handler


class Student:
    students_unit_selection_information= []
    execute_counter = 0

    def __init__(self,first_name,last_name,student_code,national_code,major):
        self.first_name=first_name
        self.last_name=last_name
        self.student_code=student_code
        self.national_code=national_code
        self.major=major
        self.number_of_units = ''
        self.courses_list=[]

    def check_unit_numbers_range(self):
        if self.number_of_units > 20 or self.number_of_units < 10:
            return False
        else:
            return True

    def specify_number_of_units(self):
        with open('students_courses.json', 'r') as file:
            flag = 0
            data = json.load(file)
            for i,student in enumerate(data):
                if student['student_code'] == self.student_code:
                    flag = 1
                    break
            if flag == 1:
                student_courses=data[i]
                self.number_of_units=student_courses['number_of_units']
            elif flag == 0:
                self.number_of_units = 0

    def select_units(self, course_name):
        if self.number_of_units == '':
            self.specify_number_of_units()
        if Student.execute_counter == 0:
            with open('students_courses.json','r') as file:
                data=json.load(file)
                if data:
                    for dictionary in data:
                        Student.students_unit_selection_information.append(dictionary)
        if self.number_of_units < 20:
            with open('courses.json','r') as file:
                data=json.load(file)
                for course in data:
                    if course['course_name'] == course_name:
                        if course['unit']+self.number_of_units > 20:
                            print("you can Not take tis course because your units summation is more than 20 units ")
                            break
                        else:
                            if self.number_of_units == 0:
                                c_list=file_handler.search_in_file('courses.json','course_name',course_name)
                                dictionary=c_list[0]
                                teacher_name = dictionary['teacher_name']
                                unit = dictionary['unit']
                                course_group = dictionary['course_group']
                                capacity = dictionary['capacity']
                                chosen_course = course.Course.add_course(course_name, teacher_name, unit,
                                                                         capacity, course_group)
                                if chosen_course.check_capacity():
                                    taken_course_information={'course_name':course_name,'teacher_name':teacher_name,
                                                              'unit':unit,'course_group':course_group,'course_confirm':0}
                                    self.courses_list.append(taken_course_information)
                                    self.number_of_units+=unit
                                    student_dict={'student_code':self.student_code,
                                                  'number_of_units':self.number_of_units
                                                  ,'course_list':self.courses_list}
                                    Student.students_unit_selection_information.append(student_dict)








    @classmethod
    def add_student(cls,first_name,last_name,student_code,national_code,major):
        return cls(first_name=first_name,last_name=last_name,student_code=student_code,national_code=national_code,major=major)

    def show_choosable_courses(self):
        choosable_courses=[]
        with open('courses.json','r') as json_file:
            data=json.load(json_file)
            for course in data:
                if course['course_group'] == self.major:
                    choosable_courses.append(course)
        return choosable_courses








