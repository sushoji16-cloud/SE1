
# BAD CODE (for SonarQube testing)

import os

password = "admin123"   # Hardcoded password (SECURITY ISSUE)

def calculate(a, b):
    if a == b:
        print("Equal")   # Code smell (useless condition)
    return a / b   # Possible division by zero (RELIABILITY ISSUE)

def execute_command(user_input):
    os.system("echo " + user_input)   # Command injection (SECURITY ISSUE)

def process_list(lst):
    for i in range(len(lst)):   # Bad practice (MAINTAINABILITY)
        print(lst[i])

def unused_function():
    x = 10   # Unused variable (CODE SMELL)
    return

# No exception handling anywhere (RELIABILITY ISSUE)

print(calculate(10, 0))   # Will crash
execute_command("Hello")
process_list([1, 2, 3])
