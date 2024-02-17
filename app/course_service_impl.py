
from typing import List
from app.course_service import CourseService

class CourseServiceImpl(CourseService):
  """
  Please implement the CourseService interface according to the requirements.
  """

  def __init__(self):
    self.course_id = 0
    self.assignment_id = 0
    self.db = {}

  # Course implementation

  def get_courses(self):
    return list(self.db.values())

  def get_course_by_id(self, course_id):
    return self.db.get(course_id)

  def create_course(self, course_name):
    self.course_id += 1
    self.db[self.course_id] = {
      'assignments': {},
      'students': {}
    }
    return self.course_id

  def delete_course(self, course_id):
    if course_id in self.db:
      del self.db[course_id]
      return True
    return False

  def create_assignment(self, course_id, assignment_name):
    if course_id in self.db:
      self.assignment_id += 1
      assignment_id = self.assignment_id
      self.db[course_id]['assignments'][assignment_id] = {
        'assignment_name': assignment_name,
        'assignment_sum': 0,
        'assignment_submission_amount': 0
      }
      return assignment_id
    return None

  def enroll_student(self, course_id, student_id):
    if course_id in self.db:
      self.db[course_id]['students'][student_id] = {
        'submissions': {},
        'student_sum': 0,
        'student_submission_amount': 0
      }
      return True
    return False

  def dropout_student(self, course_id, student_id):
    if course_id in self.db and student_id in self.db[course_id]['students']:
      student = self.db[course_id]['students'][student_id]
      for assignment_id, submission in student['submissions'].items():
        grade = submission['grade']
        self.db[course_id]['assignments'][assignment_id]['assignment_sum'] -= grade
        self.db[course_id]['assignments'][assignment_id]['assignment_submission_amount'] -= 1
      del self.db[course_id]['students'][student_id]
      return True
    return False

  def submit_assignment(self, course_id, student_id, assignment_id, grade: int):
    if course_id in self.db and student_id in self.db[course_id]['students'] and assignment_id in self.db[course_id]['assignments']:
      self.db[course_id]['students'][student_id]['submissions'][assignment_id] = {
        'grade': grade
      }
      self.db[course_id]['students'][student_id]['student_sum'] += grade
      self.db[course_id]['students'][student_id]['student_submission_amount'] += 1
      self.db[course_id]['assignments'][assignment_id]['assignment_sum'] += grade
      self.db[course_id]['assignments'][assignment_id]['assignment_submission_amount'] += 1
      return True
    return False

  def get_student_grade_avg(self, course_id, student_id) -> int:
    return super().get_student_grade_avg(course_id, student_id)
  
  def get_assignment_grade_avg(self, course_id, assignment_id) -> int:
    return super().get_assignment_grade_avg(course_id, assignment_id)
  
  def get_top_five_students(self, course_id) -> List[int]:
    return super().get_top_five_students(course_id)
  



