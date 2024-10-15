import sys 

class StdinReader:

    def __init__(self):
        pass

    def read_stdin(self):
    
        input_list = [line.strip() for line in sys.stdin]

        return input_list
    

    def write_read_stdin(self, output: str):

        print(output)

        input_list = self.read_stdin()

        return input_list
    
    def write_stdin(self, output: str):

        print(output)


