import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    # @classmethod
    # def tearDownClass(cls):
    #     print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp1 = Employee(firstName='Boy', lastName='Claessen', pay=6000, bonus=500)
        self.emp2 = Employee(firstName='Jan', lastName='van der Jeugd', pay=4500, bonus=1000)

    # def tearDown(self):
    #     print('tearDown\n')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp1.fullname, 'Boy Claessen')
        self.assertEqual(self.emp2.fullname, 'Jan van der Jeugd')

    def test_annualSalary(self):
        print('test_annualSalary')
        self.assertEqual(self.emp1.annualSalary, 72500)
        self.assertEqual(self.emp2.annualSalary, 55000)

if __name__ == '__main__':
    unittest.main()
