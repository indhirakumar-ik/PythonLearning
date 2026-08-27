def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File {filename} not found"
    except Exception as e:
        return f"Error reading file: {e}"

write_to_file("my_notes.txt", "Hi i'm Indhirakumar")
content = read_from_file("my_notes.txt")
print(content)

def append_to_file(filename, new_content):
    try:
        with open(filename, 'a') as file:  # 'a' for append mode
            file.write(f"\n{new_content}")
        print(f"Successfully appended to {filename}")
    except Exception as e:
        print(f"Error appending to file: {e}")

def read_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]  # Remove newline characters
    except Exception as e:
        return [f"Error: {e}"]

append_to_file("my_notes.txt", "a final Year student")
append_to_file("my_notes.txt", "DSA problem solver")

lines = read_lines("my_notes.txt")
for i, line in enumerate(lines, 1):
    print(f"Line {i}: {line}")