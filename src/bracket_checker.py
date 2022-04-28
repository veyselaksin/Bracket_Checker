"""
TGA Bracket Checker Interview Question.

This module contains the Checker class to check if brackets are used correctly. This class takes string value.
>> e.g. usage: checker = Checker('{()}[]')
Also our class has isBalanced function. This function controls the usage of brackets that inside the given string value.
If this usage is correct, function returns "YES" value and if it's not, function returns "NO" value.
"""

class Checker:

    open_brackets = ["{", "[", "("]
    close_brackets = ["}", "]", ")"]
    brackets = dict(zip(open_brackets, close_brackets))
    stack = list()

    def __init__(self, string):
        self.string = string

    def isBalanced(self):
        
        for i in self.string:
            if i in self.open_brackets:
                self.stack.append(i)

            elif i in self.close_brackets:
                if not self.stack or i != self.brackets[self.stack.pop()]:
                    return "NO"
        
        return "YES"

