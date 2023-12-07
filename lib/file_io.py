def write_file(file_name, file_content):
    with open(f"{file_name}.txt", 'w') as file:
        file.write(file_content)
    print("File written successfully!")

write_file(file_name="file", file_content="This is a test content.")
   
def append_file(file_name, append_content):
    with open(f"{file_name}.txt", 'a') as file:
        file.write(append_content)
    print("Content appended successfully!")

append_file(file_name="file", append_content="This is a test content.")

def read_file(file_name):
    with open(f"{file_name}.txt", 'r') as file:
            content = file.read()
    return content
    