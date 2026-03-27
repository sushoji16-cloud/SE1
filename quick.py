# GOOD CODE (Clean version)

import subprocess

def calculate(a, b):
    try:
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    except Exception as e:
        return str(e)

def execute_command(user_input):
    # Safe command execution
    result = subprocess.run(
        ["echo", user_input],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout

def process_list(lst):
    for item in lst:   # Better loop
        print(item)

def main():
    print(calculate(10, 2))
    print(execute_command("Hello"))
    process_list([1, 2, 3])

if __name__ == "__main__":
    main()
