#!/usr/bin/env python3
import argparse

class AliSahinInterpreter:
    def __init__(self, filename):
        self.code = self.read_file(filename).split()
        self.memory = [0] * 30000  
        self.pointer = 0
        self.code_pointer = 0

    def read_file(self, filename):
        """Read the file contents and return as a string."""
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise Exception(f"Error: File '{filename}' not found.")
        except IOError:
            raise Exception(f"Error: Could not read file '{filename}'.")

    def interpret(self):
        try:
            while self.code_pointer < len(self.code):
                command = self.code[self.code_pointer]
                if command == 'ali':
                    self.pointer += 1
                    if self.pointer >= len(self.memory):
                        raise Exception("Error: Memory pointer out of bounds (right).")
                elif command == 'sahin':
                    self.pointer -= 1
                    if self.pointer < 0:
                        raise Exception("Error: Memory pointer out of bounds (left).")
                elif command == 'kas':
                    self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
                elif command == 'tek':
                    self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
                elif command == 'kasistan':
                    print(chr(self.memory[self.pointer]), end='')
                elif command == 'alisah':
                    user_input = input()
                    self.memory[self.pointer] = (self.memory[self.pointer] + self.validate_input(user_input)) % 256
                elif command == 'tekkas':
                    if self.memory[self.pointer] == 0:
                        self.jump_forward()
                elif command == 'alisahin':
                    if self.memory[self.pointer] != 0:
                        self.jump_backward()
                elif command == 'unibrow':
                    self.memory[self.pointer] = (self.memory[self.pointer] + 65) % 256
                elif command == 'nejatjobs':
                    self.memory[self.pointer] = (self.memory[self.pointer] + 10) % 256
                else:
                    raise Exception(f"Error: Unknown command '{command}'.")
                self.code_pointer += 1
        except IndexError:
            raise Exception("Error: Looping commands are not balanced.")

    def jump_forward(self):
        open_brackets = 1
        while open_brackets > 0:
            self.code_pointer += 1
            if self.code_pointer >= len(self.code):
                raise Exception("Error: 'tekkas' without matching 'alisahin'.")
            if self.code[self.code_pointer] == 'tekkas':
                open_brackets += 1
            elif self.code[self.code_pointer] == 'alisahin':
                open_brackets -= 1

    def jump_backward(self):
        open_brackets = 1
        while open_brackets > 0:
            self.code_pointer -= 1
            if self.code_pointer < 0:
                raise Exception("Error: 'alisahin' without matching 'tekkas'.")
            if self.code[self.code_pointer] == 'tekkas':
                open_brackets -= 1
            elif self.code[self.code_pointer] == 'alisahin':
                open_brackets += 1

    def validate_input(self, user_input):
        """Validate and convert the user input to an integer."""
        try:
            return int(user_input)
        except ValueError:
            raise Exception("Error: Input must be an integer.")

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
