import unittest
from ItEmp import ItEmp


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = ItEmp('Svet', 'Oliin')

    def test_name(self):
        self.assertEqual(self.emp.name, 'Svet')
        self.assertEqual(self.emp.surname, 'Oliin')

    def test_empty_position(self):
        self.assertIsNone(self.emp.pos)

    def test_empty_skills(self):
        self.assertEqual(len(self.emp.skills), 0)

    def test_add_position(self):
        self.emp.set_pos('Qa')
        self.assertEqual(self.emp.pos, 'Qa')

    def test_add_skill(self):
        self.emp.add_skills('jira')
        self.assertIn('jira', self.emp.skills)

    def test_add_skill_len(self):
        self.emp.add_skills('jira')
        self.assertEqual(len(self.emp.skills), 1)

    def test_add_2_skills_len(self):
        self.emp.add_skills('jira')
        self.emp.add_skills('git')
        self.assertEqual(len(self.emp.skills), 2)

    def test_add_emp_skill_len(self):
        self.emp.add_skills('')
        self.assertEqual(len(self.emp.skills), 0)

    def test_full_name(self):
        self.assertEqual(self.emp.full_name(), 'Svet Oliin')


if __name__ == "__main__":
    unittest.main()
