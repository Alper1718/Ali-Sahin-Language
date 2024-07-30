# AliSahin Language and Interpreter

AliSahin is an esoteric programming language designed for educational purposes. It features a minimalistic set of commands to manipulate memory and control program flow. This repository includes an interpreter to execute .alisahin files.

## Features

    Memory: 30,000 cells.
    Pointer Manipulation: Move and adjust the memory pointer.
    Basic I/O: Read and print characters.
    Looping Constructs: Conditional loops using tekkas and alisahin.

## Commands
### Memory Pointer

    ali - Increment the memory pointer.
    sahin - Decrement the memory pointer.

### Memory Operations

    kas - Increment the value at the current memory pointer.
    tek - Decrement the value at the current memory pointer.

### Input/Output

    kasistan - Print the character at the current memory pointer.
    alisah - Read a character from input and store it at the current memory pointer.

### Looping

    tekkas - Start a loop. If the value at the current memory pointer is zero, jump forward to the corresponding alisahin.
    alisahin - End a loop. If the value at the current memory pointer is not zero, jump back to the corresponding tekkas.

### Additional Commands

    unibrow - Increment the value at the current memory pointer by 65.
    nejatjobs - Increment the value at the current memory pointer by 10.

## Installation

  ### Clone the Repository:

'''sh
git clone https://github.com/yourusername/alisahin.git
cd alisahin
'''

### Make the Interpreter Executable:

'''sh
chmod +x alisahin
'''

### Add to PATH (Optional):
Create a symbolic link in a directory included in your PATH:

'''sh
    ln -s /path/to/alisahin /usr/local/bin/alisahin
'''

## Usage

To run an .alisahin file, use the following command:

'''sh
alisahin path/to/yourfile.alisahin
'''

## Example
This line will print ALPER
'''
ali unibrow kasistan ali unibrow nejatjobs kas kasistan ali unibrow nejatjobs kas kas kas kas kas kasistan ali unibrow kas kas kas kas kasistan sahin kas kas kasistan
'''
