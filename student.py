import json
import course


class Student:
    def __init__(self,first_name,last_name,student_code,national_code,major):
        self.first_name=first_name
        self.last_name=last_name
        self.student_code=student_code
        self.national_code=national_code
        self.major=major

    def check_range_unit_numbers(self):
         return f"this method checks if the total number of units that a student takes would not be more than 20" \
                f" and not be less than10 units."

    def edit_info(self,**kwargs):
        '''
        this method takes the attributes of an object that we want them to change
         and then edit the attributes of that object and returns the edited object.
        '''
        self.__dict__.update((k, v) for k, v in kwargs.items())
        return self

    def select_units(self,course_name):
        return f"this method adds chosen course to the students courses list and as many as course units " \
               f"adds to students number of units attribute." \
               f"this method also calls the reduce_capacity method of the course class"

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

    def __str__(self):
        return f"this method returns student's information."






