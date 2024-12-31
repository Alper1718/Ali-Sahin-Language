#!/usr/bin/env python3
import argparse
import re
import os

class AliSahinInterpreter:
    def __init__(self, filename):
        self.code = self.read_file(filename)
        self.memory = [0] * 30000
        self.pointer = 0
        self.functions = {}
        self.parsed_files = set()
        self.overdrive_enabled = False

    def read_file(self, filename):
        """Read the file contents and return as a list of lines."""
        try:
            with open(filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            raise Exception(f"Error: File '{filename}' not found.")
        except IOError:
            raise Exception(f"Error: Could not read file '{filename}'.")

    def parse(self):
        current_function = None
        for line in self.code:
            line = line.strip()
            if line.startswith(";"):  # Skip comment lines
                continue
            
            tokens = re.split(r'\s+|\b', line)
            tokens = [t for t in tokens if t]
            if not tokens:
                continue
            
            if tokens[0] == "nejatjobs":
                if len(tokens) < 2 or "{" not in tokens:
                    raise Exception("Error: 'nejatjobs' must be followed by a function name and '{'.")
                current_function = tokens[1]
                self.functions[current_function] = []
            elif "}" in tokens and current_function:
                current_function = None
            elif current_function:
                self.functions[current_function].extend(tokens)
            elif tokens[0] == "unibrow":
                if len(tokens) < 2:
                    raise Exception("Error: 'unibrow' must be followed by a filename.")
                self.import_file(tokens[1])
            elif tokens[0] == "overdrive":
                self.overdrive_enabled = True
            else:
                self.execute_line(tokens)


    def import_file(self, filename):
        """Import functions from another .alisahin file."""
        if filename in self.parsed_files:
            return

        if not filename.endswith(".alisahin"):
            filename += ".alisahin"
        
        if not os.path.isfile(filename):
            raise Exception(f"Error: Imported file '{filename}' not found.")

        imported_code = self.read_file(filename)
        imported_interpreter = AliSahinInterpreter(filename)
        imported_interpreter.code = imported_code
        imported_interpreter.parse()

        for func_name, func_commands in imported_interpreter.functions.items():
            if func_name in self.functions and not self.overdrive_enabled:
                raise Exception(f"Error: Function '{func_name}' in '{filename}' conflicts with an existing function.")
            self.functions[func_name] = func_commands
        
        self.parsed_files.add(filename)

    def execute_line(self, tokens):
        """Execute a single line of commands."""
        for command in tokens:
            if command == "ali":
                self.pointer += 1
                if self.pointer >= len(self.memory):
                    raise Exception("Error: Memory pointer out of bounds (right).")
            elif command == "sahin":
                self.pointer -= 1
                if self.pointer < 0:
                    raise Exception("Error: Memory pointer out of bounds (left).")
            elif command == "kas":
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
            elif command == "tek":
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
            elif command == "kasistan":
                print(chr(self.memory[self.pointer]), end='')
            elif command == "alisah":
                user_input = input()
                self.memory[self.pointer] = (self.memory[self.pointer] + self.validate_input(user_input)) % 256
            elif command == "tekkas":
                if self.memory[self.pointer] == 0:
                    return
            elif command == "alisahin":
                if self.memory[self.pointer] != 0:
                    return

            elif command in self.functions:
                self.execute_function(command)
            else:
                raise Exception(f"Error: Unknown command '{command}'.")

    def execute_function(self, function_name):
        """Execute a defined function while maintaining pointer position."""
        if function_name not in self.functions:
            raise Exception(f"Error: Function '{function_name}' is not defined.")
        
        function_commands = self.functions[function_name]
        self.execute_line(function_commands)

    def validate_input(self, user_input):
        try:
            return int(user_input)
        except ValueError:
            raise Exception("Error: Input must be an integer.")

    def interpret(self):
        self.parse() 

def main():
    parser = argparse.ArgumentParser(description='Run an .alisahin file with the AliSahinInterpreter.')
    parser.add_argument('filename', type=str, help='The path to the .alisahin file')
    args = parser.parse_args()

    try:
        interpreter = AliSahinInterpreter(args.filename)
        interpreter.interpret()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
