from typing import NewType
from operation import operation
from Operator import Operator 


class CalculatorController:

    def __init__(self):
        #Dictionary
        self.Operations = {
            operation.Add      : Operator("Addition", lambda x, y : x + y),
            operation.Subtract : Operator("Subtraction", lambda x, y : x - y),
            operation.Multiply : Operator("Multiplication", lambda x, y : x * y),
            operation.Divide   : Operator("Division", lambda x, y : x / y) 
        }

        print( self.Operations[operation.Add ].execute([1, 2]))


CalculatorController()


