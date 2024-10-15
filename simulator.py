import subprocess
import json

class SimulateFile:

    def __init__(self, simulation_file: str):
        self.simulation_file = f'{simulation_file}.py'
        self.current_input = None

    def reading_input(self, input_file_name):
        
        # reading an input file here, json?

        self.simulation_inputs = ["This is input line 1\nThis is input line 2\nAnother input line\n"]

        pass

    def run_simulation(self):

        command = ['python', self.simulation_file]  # Use 'python' instead of 'python3' if needed

        # run approximation as subprocess
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,  # output from approximation file
            stderr=subprocess.PIPE,  # error from approximation file
            text=True,               # decode output to string
            bufsize=1,               # line-buffered output
            universal_newlines=True   # newlines are handled properly
        )    

        # Loop to handle ongoing output from file2.py
        while True:
            output = process.stdout.readline()

            # break if approximation is done
            if len(output) >= 3:
                if output[:3] == 'end' and process.poll() is not None:
                    break
                
            # handle the query
            if output:
                output = output.strip()
                print(f"File 2 output: {output}")
                
                # Respond based on the output
                if "Message 3" in output:
                    print("File 1 detected Message 3, responding now...")
                elif "Final message" in output:
                    print("File 1 detected the final message, doing something special...")


        stdout, stderr = process.communicate(input=self.simulation_inputs.encode())  # Convert input to bytes

        

# Communicate sends the input and retrieves output

# Print the output from file2.py
print("Output from file2.py:")
print(stdout.decode())  # Decode bytes back to string

# If there were any errors, print them
if stderr:
    print("Errors:")
    print(stderr.decode())