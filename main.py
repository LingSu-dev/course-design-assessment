from app.course_service_impl import CourseServiceImpl

if __name__ == "__main__":
  course_service = CourseServiceImpl()
  print(course_service.courses)

  # Start receiving requests...

  course_service.create_course("CSCC73")
  result = course_service.get_courses()
  print(result)
