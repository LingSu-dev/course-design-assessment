from app.course_service_impl import CourseServiceImpl

if __name__ == "__main__":
  course_service = CourseServiceImpl()
  print(course_service.courses)

  # Start receiving requests...

  course_service.create_course("CSCC73")
  print(course_service.get_courses())
  print(course_service.get_course_by_id(1))
  print(course_service.delete_course(1))
  print(course_service.get_courses())
  course_service.create_course("CSCC73")
  print(course_service.create_assignment(2, "Algorithms 1"))
  print(course_service.get_courses())

