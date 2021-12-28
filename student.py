import json
import log
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
        self.chosen_courses_objects = []

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

    @staticmethod
    def find_and_make_an_instance(course_name):
        c_list = file_handler.search_in_file('courses.json', 'course_name', course_name)
        dictionary = c_list[0]
        chosen_course = course.Course.add_course(course_name, dictionary['teacher_name'], dictionary['unit'],
                                                 dictionary['capacity'], dictionary['course_group'])
        return chosen_course

    def select_units(self, course_name):
        if self.number_of_units == '':
            self.specify_number_of_units()
        if self.number_of_units < 20:
            with open('courses.json','r') as file:
                data=json.load(file)
            for course in data:
                if course['course_name'] == course_name:
                    if course['unit']+self.number_of_units > 20:
                        print("you can Not take this course because your units summation is more than 20 units ")
                        break
                    else:
                        chosen_course=Student.find_and_make_an_instance(course_name)
                        if chosen_course.check_capacity():
                            self.number_of_units += chosen_course.unit
                            self.courses_list.append({'course_name':course_name,
                                                      'teacher_name':chosen_course.teacher_name,
                                                      'unit':chosen_course.unit,
                                                      'course_group':chosen_course.course_group,
                                                      'course_confirm':0
                                                    })
                            self.chosen_courses_objects.append(chosen_course)
                            log.info_logger.info(f"the student with {self.student_code} student code"
                                                 f" has took {course_name} course.")
                        else:
                            print("this course doesn't have capacity to take.")
                        break
        else:
            print("you can not take more than 20 units.")
        return self

    def final_unit_selection_registration(self):
        check_units=self.check_unit_numbers_range()
        if check_units:
            self.chosen_courses_objects=[course_object.reduce_capacity()
                                         for course_object
                                         in self.chosen_courses_objects]
            search_result=file_handler.search_in_file('students_courses.json','student_code',self.student_code)
            if search_result:
                with open('students_courses.json', 'r') as file:
                    Student.students_unit_selection_information = json.load(file)
                    for item in Student.students_unit_selection_information:
                        if item['student_code'] == self.student_code:
                            item['number_of_units'] = self.number_of_units
                            for dictionary in self.courses_list:
                                item['courses_list'].append(dictionary)
                            break
                with open('students_courses.json','w') as file:
                    json.dump(Student.students_unit_selection_information,file)
                Student.execute_counter += 1
                return True
            else:
                student_courses={'student_code':self.student_code,
                                 'number_of_units':self.number_of_units,
                                 'courses_list':self.courses_list
                }
                Student.students_unit_selection_information.append(student_courses)
                if Student.execute_counter == 0:
                    with open('students_courses.json','r') as file:
                        data=json.load(file)
                        if data:
                            for dictionary in data:
                                Student.students_unit_selection_information.append(dictionary)
                with open('students_courses.json','w') as file:
                    json.dump(Student.students_unit_selection_information,file)
                Student.execute_counter += 1
                log.info_logger.info(f"final unit selection of student with {self.student_code} student code"
                                     f"has been done.")
                return True
        else:
            print("your number of units should be in range 10 to 20.")
            return False

    def prevent_duplicate_courses_in_unit_selection(self,course_name):
        flag = 0
        search_result = file_handler.search_in_file('students_courses.json', 'student_code', self.student_code)
        if search_result:
            if self.courses_list:
                for item in self.courses_list:
                    if item['course_name'] == course_name:
                        flag = 1
                        break
            with open('students_courses.json','r') as file:
                data=json.load(file)
                for dictionary in data:
                    if dictionary['student_code'] == self.student_code:
                        for item in dictionary['courses_list']:
                            if item['course_name'] == course_name:
                                flag = 1
                                break
        else:
            for item in self.courses_list:
                if item['course_name'] == course_name:
                    flag = 1
                    break
        if flag == 1:
            return False
        elif flag == 0:
            return True

    def show_chosen_courses(self):
        search_result = file_handler.search_in_file('students_courses.json', 'student_code', self.student_code)
        print(f"the numbers of units you have chosen: {self.number_of_units}")
        print("so far you have chosen this courses:")
        if search_result:
            search_result=search_result[0]
            for dictionary in search_result['courses_list']:
                print(dictionary)
        for item in self.courses_list:
            print(item)

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








