import operation


class CalculatorUI:

    def display_operations(self):
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

    def get_operation(self)->operation:
        
        self.display_operations()
        selected_op: str = input('Select an operation: ')

        try:
            selected_op_int: int = int(selected_op)
        except:
            selected_op_int = None

        if selected_op_int == 1 :
            return operation.Add
        
        if selected_op_int == 2 :
            return operation.Subtract

        if selected_op_int == 3 :
            return operation.Multiply

        if selected_op_int == 4 :
            return operation.Divide

        return None
        

    def get_argument(self)->float:

        try:
            input_variable: str = input("Enter Value:")
            input_variable_float: float = float(input_variable)
            return input_variable_float
        except:
            return None
