import unittest
from class_definitions import student as s

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Smith', 'Johnny', 'Culinary', 3.25)

    def tearDown(self):
        del self.student

    def test_object_created_required_attribute(self):
        self.assertEqual(self.student.last_name, 'Smith')
        self.assertEqual(self.student.first_name, 'Johnny')
        self.assertEqual(self.student.major, 'Culinary')

    def test_object_created_all_attributes(self):
        student = s.Student('Smith', 'Johnny', 'Culinary', 3.25) # this is not self.person from setUp, but local
        assert student.last_name == 'Smith'                 # note no self here on person or assert
        assert student.first_name == 'Johnny'
        assert student.major == 'Culinary'
        assert student.gpa == 3.25

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Smith, Johnny has major Culinary with gpa: 3.25')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            a = s.Student('123', 'Johnny', 'Culinary')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            a = s.Student('Smith', '123', 'Culinary')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            a = s.Student('Smith', 'Johnny', '123')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            a = s.Student('Smith', 'Johnny', 'Culinary', 6.00)

if __name__ == '__main__':
    unittest.main()
