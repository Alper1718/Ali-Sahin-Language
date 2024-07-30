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
        with open(filename, 'r') as file:
            return file.read()

    def interpret(self):
        while self.code_pointer < len(self.code):
            command = self.code[self.code_pointer]
            if command == 'ali':
                self.pointer += 1
            elif command == 'sahin':
                self.pointer -= 1
            elif command == 'kas':
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
            elif command == 'tek':
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
            elif command == 'kasistan':
                print(chr(self.memory[self.pointer]), end='')
            elif command == 'alisah':
                self.memory[self.pointer] = ord(input()[0])
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
            self.code_pointer += 1

    def jump_forward(self):
        open_brackets = 1
        while open_brackets > 0:
            self.code_pointer += 1
            if self.code[self.code_pointer] == 'tekkas':
                open_brackets += 1
            elif self.code[self.code_pointer] == 'alisahin':
                open_brackets -= 1

    def jump_backward(self):
        open_brackets = 1
        while open_brackets > 0:
            self.code_pointer -= 1
            if self.code[self.code_pointer] == 'tekkas':
                open_brackets -= 1
            elif self.code[self.code_pointer] == 'alisahin':
                open_brackets += 1

def main():
    parser = argparse.ArgumentParser(description='Run an .alisahin file with the AliSahinInterpreter.')
    parser.add_argument('filename', type=str, help='The path to the .alisahin file')
    args = parser.parse_args()

    interpreter = AliSahinInterpreter(args.filename)
    interpreter.interpret()

if __name__ == '__main__':
    main()
