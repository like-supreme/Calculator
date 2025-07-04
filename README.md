# Calculator
A simple Python-based CLI calculator that supports basic arithmetic operations with a clean user interface and recursive loop logic.
# 🧮 CLI Calculator in Python

This is a beginner-friendly, terminal-based calculator written in Python.  
The program supports basic arithmetic operations like addition, subtraction, multiplication, and division.  
It uses a modular structure with custom-designed ASCII UI and clean function separation.

## 🚀 Features
- Simple and interactive terminal UI
- Supports: `+`, `-`, `*`, `/`
- Uses function mapping for dynamic operator selection
- Recursively restarts if the user wants to continue
- Clears the screen between operations
- Modularized code (divided into three separate files)

## 📁 File Structure
├── main.py # Main calculator logic
├── operator_functions.py # Arithmetic function definitions
└── art.py # Contains the ASCII art/logo

## 📦 How to Run

Make sure you have Python 3 or higher installed.
what is your first number.
> 10
+
-
*
/
Pick an operator.
> +

What is your second number ?
> 5

Your first number is: 10. and your second number is: 5. You selected the +. Your answer is 15.

Wanna continue? type y for continue, n for exit
> y
 Logo Preview
>  _____________________
|  _________________  |
| | Like-supremegit | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

