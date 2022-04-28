# BRACKET CHECKER

There is a class called Checker in the algorithm and this class takes a string value. The Checker class also has a function called isBalanced. This function checks whether the parentheses in the given string are used correctly. Returns "YES" if it is used correctly, and "NO" if not.


While creating the algorithm, two arrays named open_brackets and close_brackets were used.

```python
open_brackets = ["{", "[", "("]
close_brackets = ["}", "]", ")"]
```

These sequences represent the opening and closing tags of the parentheses. Sequences of opening and closing tags are combined with each opening element with its own closing element using the zip function. Then, using the dictionary structure, the key-value relationship is obtained.

``` python
open_brackets = ["{", "[", "("]
close_brackets = ["}", "]", ")"]
brackets = dict(zip(open_brackets, close_brackets))
```

Each opening tag is passed into an array called stack. When the closing tag is encountered, the value of the topmost opening tag in the stack is compared with the value of the closing tag. If the values are not equal, the function returns "NO". Also, if the stack is not empty, the function returns "NO". If the operations are successful, the function returns "YES" by default.

```python
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

```

## Usage
```sh
git clone https://github.com/veyselaksin/Bracket_Checker.git

cd Bracket_Checker
python -m test.bc_test.py

```
