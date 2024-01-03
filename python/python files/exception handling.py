def divide_numbers(x, y):
    try:
        result = x / y
        print("Result", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)
    else:
        print("No exceptions occurred.")
    finally:
        print("this is the finally block")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print("File content:")
            print(data)
    except FileNotFoundError:
        print("Error: File not found at path ")
    except PermissionError:
        print("Error: Permission denied while reading the file.")
    except Exception as e:
        print("Unexpected error:", e)
    else:
        print("File read operation successful.")
    finally:
        print("File reading process completed.")

def raise_custom_exception(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        elif age < 18:
            raise ValueError("You must be 18 or older.")
        else:
            print("Access granted.")
    except ValueError as e:
        print("Error:", e)
    finally:
        print("Exception handling completed.")

# Example 1: Handling division exceptions
divide_numbers(10, 2)
divide_numbers(5, 0)
divide_numbers("a", 2)

# Example 2: Handling file-related exceptions
read_file("nonexistent_file.txt")
read_file("Examplefile.txt")

# Example 3: Raising custom exceptions
raise_custom_exception(25)
raise_custom_exception(-5)
