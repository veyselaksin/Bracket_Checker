import unittest
from src.bracket_checker import Checker

class BCTest(unittest.TestCase):

    def test_empty_string(self):
        checker = Checker("")
        result = checker.isBalanced()
        self.assertEqual(result, "YES")

    def test_single_bracket(self):
        checker = Checker("{}")
        result = checker.isBalanced()
        self.assertEqual(result, "YES")
    
    def test_multiple_balanced_brackets(self):
        checker = Checker("{()[]{([[]])}}")
        result = checker.isBalanced()
        self.assertEqual(result, "YES")
    
    def test_multiple_unbalanced_brackets(self):
        checker = Checker("[(}{){())][{}]}]")
        result = checker.isBalanced()
        self.assertEqual(result, "NO")
    
    def test_multiple_balanced_brackets2(self):
        checker = Checker("{}[](({{[]}}))")
        result = checker.isBalanced()
        self.assertEqual(result, "YES")
    
    def test_multiple_unbalanced_brackets2(self):
        checker = Checker("{[{]}]([])")
        result = checker.isBalanced()
        self.assertEqual(result, "NO")
    

if __name__ == "__main__":
    unittest.main()
