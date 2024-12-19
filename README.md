# AliSahin Language and Interpreter

AliSahin is an esoteric programming language designed for educational purposes. It features a minimalistic set of commands to manipulate memory, define functions, and control program flow. This repository includes an interpreter to execute `.alisahin` files.

## Features

- **Memory**: 30,000 cells.
- **Pointer Manipulation**: Move and adjust the memory pointer.
- **Basic I/O**: Read and print characters.
- **Looping Constructs**: Conditional loops using `tekkas` and `alisahin`.
- **Functions**: Define reusable code blocks with `nejatjobs`.
- **File Importing**: Import functions from other `.alisahin` files with `unibrow`.
- **Overriding Functions**: Use the `overdrive` keyword to overwrite existing functions.

## Commands

### Memory Pointer

- `ali` - Increment the memory pointer.
- `sahin` - Decrement the memory pointer.

### Memory Operations

- `kas` - Increment the value at the current memory pointer.
- `tek` - Decrement the value at the current memory pointer.

### Input/Output

- `kasistan` - Print the character at the current memory pointer.
- `alisah` - Read a character from input and store it at the current memory pointer.

### Looping

- `tekkas` - Start a loop. If the value at the current memory pointer is zero, jump forward to the corresponding `alisahin`.
- `alisahin` - End a loop. If the value at the current memory pointer is not zero, jump back to the corresponding `tekkas`.

### Functions

- `nejatjobs functionname { ... }` - Define a function with the specified `functionname`. Code inside the curly braces will execute when the function is called.
- To **call** a function, simply write its name anywhere in the program.

### File Importing

- `unibrow filename` - Import functions from another `.alisahin` file. The filename can include or omit the `.alisahin` extension.

### Overriding Functions

- `overdrive` - Use this keyword before `unibrow` to enable function overriding. This allows imported functions to overwrite existing ones.

## Installation

### Clone the Repository:

```sh
git clone https://github.com/Alper1718/Ali-Sahin-Language.git
```

### Make the Interpreter Executable:

```sh
chmod +x alisahin.py
```

### Add to PATH (Optional):
Create a symbolic link in a directory included in your PATH:

```sh
ln -s /path/to/alisahin.py /usr/local/bin/alisahin
```

## Usage

To run an `.alisahin` file, use the following command:

```sh
alisahin path/to/yourfile.alisahin
```

## Examples

### Example 1: Printing `ALPER`

The following code prints `ALPER`:

```
nejatjobs incrementByTen {
    kas kas kas kas kas kas kas kas kas kas
}
nejatjobs makeA {
    incrementByTen
    incrementByTen
    incrementByTen
    incrementByTen
    incrementByTen
    incrementByTen
    kas kas kas kas kas
}

ali makeA kasistan incrementByTen kas kasistan kas kas kas kas kasistan ali makeA kas kas kas kas kasistan sahin kas kas kasistan
```

### Example 2: Importing and Overriding Functions

Assume we have a file `basicfunctions.alisahin` containing:

```
nejatjobs incrementByTen {
    kas kas kas kas kas kas kas kas kas kas
}
nejatjobs makeA {
    incrementByTen
    incrementByTen
    incrementByTen
    incrementByTen
    incrementByTen
    incrementByTen
    kas kas kas kas kas
}

nejatjobs Alper {
    ali makeA kasistan incrementByTen kas kasistan kas kas kas kas kasistan ali makeA kas kas kas kas kasistan sahin kas kas kasistan
}
```

To import these functions into another `.alisahin` file:

```
unibrow basicfunctions
ali Alper

```

