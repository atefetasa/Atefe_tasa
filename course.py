import json
import log
import register


class Course:
    courses = []
    execute_counter = 0

    def __init__(self,course_name,teacher_name,unit,capacity,course_group):
        self.course_name=course_name
        self.teacher_name=teacher_name
        self.unit=unit
        self.capacity=capacity
        self.course_group=course_group

    def check_capacity(self):
        try:
            if self.capacity >= 1:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            log.warning_logger.error(e)

    def reduce_capacity(self):
        self.capacity=self.capacity-1
        if Course.execute_counter == 0:
            try:
                with open('courses.json','r') as file:
                    data=json.load(file)
                    if data:
                        for dictionary in data:
                            Course.courses.append(dictionary)
            except Exception as e:
                print(e)
                log.warning_logger.error(e)
        for course in Course.courses:
            if course['course_name'] == self.course_name:
                course['capacity'] = self.capacity
                break
        with open('courses.json','w') as file:
            json.dump(Course.courses,file)
        Course.execute_counter +=1

    @classmethod
    def add_course(cls,course_name,teacher_name,unit,capacity,course_group):
        return cls(course_name=course_name,teacher_name=teacher_name,unit=unit,capacity=capacity,
                   course_group=course_group)

    def __str__(self):
        return {'course_name':self.course_name,'teacher_name':self.teacher_name,
                'unit':self.unit,'capacity':self.capacity,'course_group':self.course_group}






