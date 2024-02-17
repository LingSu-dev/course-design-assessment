import unittest
import app.course_service_impl

class TestCourseServiceImpl(unittest.TestCase):
    def setUp(self):
        self.course_service = app.course_service_impl.CourseServiceImpl()

    def test_empty_get_courses(self):
        courses = self.course_service.get_courses()
        self.assertEqual(len(courses), 0)
        self.assertEqual(courses, [])

    def test_one_get_courses(self):
        course_id = self.course_service.create_course("Math")
        courses = self.course_service.get_courses()
        self.assertEqual(courses, [(1, {'course_name': 'Math', 'assignments': {}, 'students': {}})])

    def test_many_get_courses(self):
        course_id = self.course_service.create_course("Math")
        course_id = self.course_service.create_course("Math2")
        courses = self.course_service.get_courses()
        self.assertEqual(courses, [(1, {'course_name': 'Math', 'assignments': {}, 'students': {}}), \
                                   (2, {'course_name': 'Math2', 'assignments': {}, 'students': {}})])

    def test_get_course_by_id(self):
        course_id = self.course_service.create_course("Math")
        course = self.course_service.get_course_by_id(course_id)
        self.assertEqual(course, {'assignments': {}, 'course_name': 'Math', 'students': {}})

    def test_bad_id_get_course_by_id(self):
        non_existent_course_id = 999
        course = self.course_service.get_course_by_id(non_existent_course_id)
        self.assertEqual(None, course)

    def test_create_course(self):
        course_id = self.course_service.create_course("Math")
        self.assertEqual(course_id, 1)

    def test_delete_course(self):
        course_id = self.course_service.create_course("Math")
        result = self.course_service.delete_course(course_id)
        self.assertTrue(result)
    
    def test_bad_id_delete_course(self):
        result = self.course_service.delete_course(999)
        self.assertFalse(result)

    def test_create_assignment(self):
        course_id = self.course_service.create_course("Math")
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        self.assertEqual(assignment_id, 1)
    
    def test_bad_id_create_assignment(self):
        non_existent_course_id = 999
        assignment_id = self.course_service.create_assignment(non_existent_course_id, "Homework 1")
        self.assertIsNone(assignment_id)

    def test_enroll_student(self):
        course_id = self.course_service.create_course("Math")
        result = self.course_service.enroll_student(course_id, 1)
        self.assertTrue(result)
    
    def test_bad_id_enroll_student(self):
        non_existent_course_id = 999
        result = self.course_service.enroll_student(non_existent_course_id, 1)
        self.assertFalse(result)

    def test_dropout_student(self):
        course_id = self.course_service.create_course("Math")
        self.course_service.enroll_student(course_id, 1)
        result = self.course_service.dropout_student(course_id, 1)
        self.assertTrue(result)
    
    def test_bad_id_dropout_student(self):
        course_id = self.course_service.create_course("Math")
        result = self.course_service.dropout_student(course_id, 1)
        self.assertFalse(result)
        result2 = self.course_service.dropout_student(999, 1)
        self.assertFalse(result2)
    
    def test_average_modification_dropout_student(self):
        course_id = self.course_service.create_course("Math")
        self.course_service.enroll_student(course_id, 1)
        self.course_service.enroll_student(course_id, 2)
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        self.course_service.submit_assignment(course_id, 1, assignment_id, 90)
        self.course_service.submit_assignment(course_id, 2, assignment_id, 80)
        
        # Test that the average is successfully modified after dropping a student
        self.course_service.dropout_student(course_id, 1)
        avg_grade = self.course_service.get_assignment_grade_avg(course_id, assignment_id)
        self.assertEqual(avg_grade, 80)

    def test_submit_assignment(self):
        course_id = self.course_service.create_course("Math")
        self.course_service.enroll_student(course_id, 1)
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        result = self.course_service.submit_assignment(course_id, 1, assignment_id, 90)
        self.assertTrue(result)
    
    def test_bad_id_submit_assignment(self):
        non_existent_course_id = 999
        non_existent_student_id = 999
        non_existent_assignment_id = 999
        course_id = self.course_service.create_course("Math")
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        self.course_service.enroll_student(course_id, 1)
        result = self.course_service.submit_assignment(non_existent_course_id, 1, assignment_id, 90)
        self.assertFalse(result)
        result2 = self.course_service.submit_assignment(course_id, non_existent_student_id, assignment_id, 90)
        self.assertFalse(result)
        result3 = self.course_service.submit_assignment(course_id, 1, non_existent_assignment_id, 90)
        self.assertFalse(result)

    def test_none_get_student_grade_avg(self):
        course_id = self.course_service.create_course("Math")
        avg_grade = self.course_service.get_student_grade_avg(999, 1)
        self.assertIsNone(avg_grade)
        avg_grade = self.course_service.get_student_grade_avg(course_id, 1)
        self.assertIsNone(avg_grade)
        
    def test_no_submission_get_student_grade_avg(self):
        course_id = self.course_service.create_course("Math")
        assignment_id = self.course_service.create_assignment(course_id, "Assignment1")
        self.course_service.enroll_student(course_id, 1)
        result = self.course_service.get_student_grade_avg(course_id, 1)
        self.assertEqual(result, 0)
        self.course_service.submit_assignment(course_id, 1, assignment_id, 90)
        result = self.course_service.get_student_grade_avg(course_id, 1)
        self.assertEqual(result, 90)

    def test_single_get_student_grade_avg(self):
        course_id = self.course_service.create_course("Math")
        self.course_service.enroll_student(course_id, 1)
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        self.course_service.submit_assignment(course_id, 1, assignment_id, 90)
        avg_grade = self.course_service.get_student_grade_avg(course_id, 1)
        self.assertEqual(avg_grade, 90)

    def test_multiple_submission_get_student_grade_avg(self):
        course_id = self.course_service.create_course("Math")
        self.course_service.enroll_student(course_id, 1)
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        self.course_service.submit_assignment(course_id, 1, assignment_id, 90)
        assignment_id = self.course_service.create_assignment(course_id, "Homework 2")
        self.course_service.submit_assignment(course_id, 1, assignment_id, 80)
        assignment_id = self.course_service.create_assignment(course_id, "Homework 3")
        self.course_service.submit_assignment(course_id, 1, assignment_id, 85)
        avg_grade = self.course_service.get_student_grade_avg(course_id, 1)
        self.assertEqual(avg_grade, 85)

    def test_none_get_assignment_grade_avg(self):
        course_id = self.course_service.create_course("Math")
        avg_grade = self.course_service.get_assignment_grade_avg(999, 1)
        self.assertIsNone(avg_grade)
        avg_grade = self.course_service.get_assignment_grade_avg(course_id, 1)
        self.assertIsNone(avg_grade)
        
    def test_no_submission_get_assignment_grade_avg(self):
        course_id = self.course_service.create_course("Math")
        assignment_id = self.course_service.create_assignment(course_id, "Assignment1")
        self.course_service.enroll_student(course_id, 1)
        result = self.course_service.get_assignment_grade_avg(course_id, assignment_id)
        self.assertEqual(result, 0)
        self.course_service.submit_assignment(course_id, 1, assignment_id, 90)
        result = self.course_service.get_assignment_grade_avg(course_id, assignment_id)
        self.assertEqual(result, 90)

    def test_single_get_assignment_grade_avg(self):
        course_id = self.course_service.create_course("Math")
        self.course_service.enroll_student(course_id, 1)
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        self.course_service.submit_assignment(course_id, 1, assignment_id, 90)
        avg_grade = self.course_service.get_assignment_grade_avg(course_id, assignment_id)
        self.assertEqual(avg_grade, 90)
    
    def test_multiple_get_assignment_grade_avg(self):
        course_id = self.course_service.create_course("Math")
        self.course_service.enroll_student(course_id, 1)
        self.course_service.enroll_student(course_id, 2)
        self.course_service.enroll_student(course_id, 3)
        assignment_id = self.course_service.create_assignment(course_id, "Homework 1")
        self.course_service.submit_assignment(course_id, 1, assignment_id, 90)
        self.course_service.submit_assignment(course_id, 2, assignment_id, 100)
        self.course_service.submit_assignment(course_id, 3, assignment_id, 80)
        avg_grade = self.course_service.get_assignment_grade_avg(course_id, assignment_id)
        self.assertEqual(avg_grade, 90)

    def test_quickselects_kth_largest_element(self):
        arr = [(1, 5), (2, 2), (3, 8), (4, 1), (5, 9), (6, 3)]
        low = 0
        high = len(arr) - 1
        selected = self.course_service.quickselect(arr, low, high, 2)
        self.assertEqual(selected, (1, 5))

    def test_get_top_five_students(self):
        course_id = self.course_service.create_course("Math")
        for i in range(1, 7):
            self.course_service.enroll_student(course_id, i)
            assignment_id = self.course_service.create_assignment(course_id, f"Homework {i}")
            self.course_service.submit_assignment(course_id, i, assignment_id, i * 10)
        top_students = self.course_service.get_top_five_students(course_id)
        self.assertEqual(top_students, [6, 5, 4, 3, 2])
    
    def test_all_ties_get_top_five_students(self):
        course_id = self.course_service.create_course("Math")
        for i in range(1, 7):
            self.course_service.enroll_student(course_id, i)
            assignment_id = self.course_service.create_assignment(course_id, f"Homework {i}")
        for i in range(1, 7):
            for j in range(1, 7):
                self.course_service.submit_assignment(course_id, i, j, 90)
        top_students = self.course_service.get_top_five_students(course_id)
        self.assertEqual(top_students, [1, 2, 3, 4, 5])
    
    def test_less_than_five_get_top_five_students(self):
        course_id = self.course_service.create_course("Math")
        for i in range(1, 4):
            self.course_service.enroll_student(course_id, i)
            assignment_id = self.course_service.create_assignment(course_id, f"Homework {i}")
            self.course_service.submit_assignment(course_id, i, assignment_id, i * 10)
        top_students = self.course_service.get_top_five_students(course_id)
        self.assertEqual(top_students, [3, 2, 1])
    
    def test_no_student_get_top_five_students(self):
        course_id = self.course_service.create_course("Math")
        top_students = self.course_service.get_top_five_students(course_id)
        self.assertEqual(top_students, [])

if __name__ == '__main__':
    unittest.main()