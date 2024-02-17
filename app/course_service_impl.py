
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
    if course_id not in self.db:
      return False

    del self.db[course_id]
    return True

  def create_assignment(self, course_id, assignment_name):
    if course_id not in self.db:
      return None

    self.assignment_id += 1
    assignment_id = self.assignment_id
    self.db[course_id]['assignments'][assignment_id] = {
      'assignment_name': assignment_name,
      'assignment_sum': 0,
      'assignment_submission_amount': 0
    }
    return assignment_id

  def enroll_student(self, course_id, student_id):
    if course_id not in self.db:
      return False

    self.db[course_id]['students'][student_id] = {
      'submissions': {},
      'student_sum': 0,
      'student_submission_amount': 0
    }
    return True

  def dropout_student(self, course_id, student_id):
    if course_id not in self.db:
      return False
    if student_id not in self.db[course_id]['students']:
      return False

    student = self.db[course_id]['students'][student_id]
    # we need to remove the submissions from our sum when removing students
    for assignment_id, submission in student['submissions'].items():
      grade = submission['grade']
      self.db[course_id]['assignments'][assignment_id]['assignment_sum'] -= grade
      self.db[course_id]['assignments'][assignment_id]['assignment_submission_amount'] -= 1

    del self.db[course_id]['students'][student_id]
    return True

  def submit_assignment(self, course_id, student_id, assignment_id, grade: int):
    if course_id not in self.db:
      return False
    if student_id not in self.db[course_id]['students']:
      return False
    if assignment_id not in self.db[course_id]['assignments']:
      return False
    
    self.db[course_id]['students'][student_id]['submissions'][assignment_id] = {
      'grade': grade
    }
    self.db[course_id]['students'][student_id]['student_sum'] += grade
    self.db[course_id]['students'][student_id]['student_submission_amount'] += 1
    self.db[course_id]['assignments'][assignment_id]['assignment_sum'] += grade
    self.db[course_id]['assignments'][assignment_id]['assignment_submission_amount'] += 1
    return True

  def get_student_grade_avg(self, course_id, student_id) -> int:
    if course_id not in self.db:
      return None
    if student_id not in self.db[course_id]['students']:
      return None

    student = self.db[course_id]['students'][student_id]
    if student['student_submission_amount'] == 0:
      return 0

    return student['student_sum'] // student['student_submission_amount']
  
  def get_assignment_grade_avg(self, course_id, assignment_id) -> int:
    if course_id not in self.db:
      return None
    if assignment_id not in self.db[course_id]['assignments']:
      return None

    assignment = self.db[course_id]['assignments'][assignment_id]
    if assignment['assignment_submission_amount'] == 0:
      return 0

    return assignment['assignment_sum'] // assignment['assignment_submission_amount']

  def partition(self, arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
      if arr[j][1] > pivot[1]: # Flipping this to > selects kth largest instead of smallest
      # We need these [1] here because our array is a tuple of (id, average)
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
        
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  

  def quickselect(self, arr, low, high, k):
    if low == high:
      return arr[low]

    pivot_index = self.partition(arr, low, high)
    if pivot_index == k:
      return arr[pivot_index]
    elif pivot_index < k:
      return self.quickselect(arr, pivot_index + 1, high, k)
    else:
      return self.quickselect(arr, low, pivot_index - 1, k)

  def get_top_five_students(self, course_id) -> List[int]:
    if course_id not in self.db:
      return []
    if len(self.db[course_id]['students']) <= 5:
      return list(self.db[course_id]['students'].keys())
    
    grades = []
    for student_id, student in self.db[course_id]['students'].items():
      grades.append((student_id, self.get_student_grade_avg(course_id, student_id)))
    top_students = []
    for top_index in range(5):
      top_students.append((self.quickselect(grades, 0, len(grades) - 1, top_index))[0])
    return top_students
  
