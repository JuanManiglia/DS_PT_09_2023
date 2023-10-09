"""
Example of a python module. Contains a variable called my_variable,
a function called my_function, and a class called MyClass.
"""

my_variable = 0

def my_function() -> int:
    """
    Example function
    """
    return my_variable
    
class MyClass:
    """
    Example class.
    """

    def __init__(self):
        self.variable = my_variable
        
    def set_variable(self, new_value: int) -> None:
        """
        Set self.variable to a new value
        """
        self.variable = new_value
        
    def get_variable(self) -> int:
        return self.variable
