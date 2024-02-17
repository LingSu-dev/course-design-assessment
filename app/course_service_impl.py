
from app.course_service import CourseService

class CourseServiceImpl(CourseService):
  """
  Please implement the CourseService interface according to the requirements.
  """

  def __init__(self):
    self.course_id = 0
    self.assignment_id = 0
    self.courses = {}

  # Course implementation
  
  def get_courses(self):
    return list(self.courses.values())
  
  def get_course_by_id(self, course_id):
    return self.courses.get(course_id)
  
  def create_course(self, course_name):
    self.course_id += 1
    self.courses[self.course_id] = {'name': course_name, 'students': [], 'assignments': []}
    return self.course_id
  
  def delete_course(self, course_id):
    if course_id in self.courses:
      del self.courses[course_id]
      return course_id
    return None

  # Assignment implementation

  def create_assignment(self, course_id, assignment_name):
    if course_id in self.courses:
      self.assignment_id += 1
      self.courses[course_id]['assignments'][self.assignment_id] = {
        'name': assignment_name,
        'grades': {},
        'avg_grades': 0
      }
      return self.assignment_id
    return None

  # Student implementation 

  def enroll_student(self, course_id, student_id):
    if course_id in self.courses:
      self.courses[course_id]['students'][student_id] = {}
    return None
      
  
  def dropout_student(self, course_id, student_id):
    if course_id in self.courses and student_id in self.courses[course_id]['students']:
      del self.courses[course_id]['students'][student_id]
  
  def submit_assignment(self, course_id, student_id, assignment_id, grade: int):
    if course_id in self.courses \
        and student_id in self.courses[course_id]['students'] \
        and assignment_id in self.courses[course_id]['assignments']:
      self.courses[course_id]['assignments'][assignment_id]['grades'][student_id] = grade
    return None
  
  # Grade averaging implementation

  """
  Computes the assignment grade average using a rolling average
  """
  def get_assignment_grade_avg(self, course_id, assignment_id) -> int:
    return super().get_assignment_grade_avg(course_id, assignment_id)
  
  """
  Computes an individual student's grade average using rolling average
  """
  def get_student_grade_avg(self, course_id, student_id) -> int:
    return super().get_student_grade_avg(course_id, student_id)
  
  """
  Compute the top five students using quickselect
  """
  def get_top_five_students(self, course_id) -> list[int]:
    return super().get_top_five_students(course_id)
  




