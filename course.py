class Course:
    '''
    this class is for courses
    '''
    def __init__(self,course_name,teacher_name,unit,capacity,course_group):
        self.course_name=course_name
        self.teacher_name=teacher_name
        self.unit=unit
        self.capacity=capacity
        self.course_group=course_group

    def edit_info(self, **kwargs):
        '''
        :param kwargs:it's the dictionary of attributes that we want to change in a coure object
        :return:it returns the edited course object with edited attributes
        '''
        self.__dict__.update((k, v) for k, v in kwargs.items())
        return self

    def check_capacity(self):
        return f"this method is for checking the remaining capacity of a course " \
               f"when a student wants to take a course."

    def reduce_capacity(self):
        return f"this method reduces a courses capacity one unit after a student take it."


    @classmethod
    def add_course(cls,course_name,teacher_name,unit,capacity,course_group):
        return f"this method makes a course object and add it to the courses."


    def __str__(self):
        return f"this method shows information about a course."




