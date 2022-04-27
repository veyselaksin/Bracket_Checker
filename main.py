# TGA MAIN FUNC


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
                if i != self.brackets[self.stack.pop()]:
                    return "NO"

        if not self.stack:
            return "YES"

