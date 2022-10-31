class Operator:

    name: str = ""
    function = None

    def __init__(self, name: str, function = None):
        self.name = name
        self.function = function 

    def execute(self, args):
        return self.function(*args)