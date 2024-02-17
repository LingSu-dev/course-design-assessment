import unittest
import app.course_service_impl

class TestCourseServiceImpl(unittest.TestCase):
    def setUp(self):
        self.course_service = app.course_service_impl.CourseServiceImpl()

    def test_get_courses(self):
        courses = self.course_service.get_courses()
        self.assertEqual(len(courses), 0)

    def test_get_course_by_id(self):
        course_id = self.course_service.create_course("Math")
        course = self.course_service.get_course_by_id(course_id)
        self.assertEqual(course, {'assignments': {}, 'students': {}})

    def test_create_course(self):
        course_id = self.course_service.create_course("Math")
        self.assertEqual(course_id, 1)

    def test_delete_course(self):
        course_id = self.course_service.create_course("Math")
        result = self.course_service.delete_course(course_id)
        self.assertTrue(result)

    def test_create_assignment(self):
        course_id = self.course_service.create_course("Math")
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        self.assertEqual(assignment_id, 1)

    def test_enroll_student(self):
        course_id = self.course_service.create_course("Math")
        result = self.course_service.enroll_student(course_id, 1)
        self.assertTrue(result)

    def test_dropout_student(self):
        course_id = self.course_service.create_course("Math")
        self.course_service.enroll_student(course_id, 1)
        result = self.course_service.dropout_student(course_id, 1)
        self.assertTrue(result)

    def test_submit_assignment(self):
        course_id = self.course_service.create_course("Math")
        self.course_service.enroll_student(course_id, 1)
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        result = self.course_service.submit_assignment(course_id, 1, assignment_id, 90)
        self.assertTrue(result)

    def test_get_student_grade_avg(self):
        course_id = self.course_service.create_course("Math")
        self.course_service.enroll_student(course_id, 1)
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        self.course_service.submit_assignment(course_id, 1, assignment_id, 90)
        avg_grade = self.course_service.get_student_grade_avg(course_id, 1)
        self.assertEqual(avg_grade, 90)

    def test_get_assignment_grade_avg(self):
        course_id = self.course_service.create_course("Math")
        self.course_service.enroll_student(course_id, 1)
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        self.course_service.submit_assignment(course_id, 1, assignment_id, 90)
        avg_grade = self.course_service.get_assignment_grade_avg(course_id, assignment_id)
        self.assertEqual(avg_grade, 90)

    def test_get_top_five_students(self):
        course_id = self.course_service.create_course("Math")
        for i in range(1, 6):
            self.course_service.enroll_student(course_id, i)
            assignment_id = self.course_service.create_assignment(course_id, f"Homework {i}")
            self.course_service.submit_assignment(course_id, i, assignment_id, i * 10)
        top_students = self.course_service.get_top_five_students(course_id)
        self.assertEqual(top_students, [5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()