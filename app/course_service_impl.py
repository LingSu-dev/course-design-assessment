
from typing import List
from app.course_service import CourseService

class CourseServiceImpl(CourseService):
  """
  Please implement the CourseService interface according to the requirements.
  """

  def __init__(self):
    self.course_id = 0
    self.assignment_id = 0
    self.courses = {}
    self.assignments = {}
    self.students = {}

  # Course implementation
  
  def get_courses(self):
    return list(self.courses.values())
  
  def get_course_by_id(self, course_id):
    return super().get_course_by_id(course_id)
  
  def create_course(self, course_name):
    return super().create_course(course_name)
  
  def delete_course(self, course_id):
    return super().delete_course(course_id)
  
  def create_assignment(self, course_id, assignment_name):
    return super().create_assignment(course_id, assignment_name)
  
  def enroll_student(self, course_id, student_id):
    return super().enroll_student(course_id, student_id)
  
  def dropout_student(self, course_id, student_id):
    return super().dropout_student(course_id, student_id)
  
  def submit_assignment(self, course_id, student_id, assignment_id, grade: int):
    return super().submit_assignment(course_id, student_id, assignment_id, grade)
  
  def get_student_grade_avg(self, course_id, student_id) -> int:
    return super().get_student_grade_avg(course_id, student_id)
  
  def get_assignment_grade_avg(self, course_id, assignment_id) -> int:
    return super().get_assignment_grade_avg(course_id, assignment_id)
  
  def get_top_five_students(self, course_id) -> List[int]:
    return super().get_top_five_students(course_id)
  



