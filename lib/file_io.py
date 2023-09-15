def write_file(file_name, file_content):
    write_file = open(f'{file_name}.txt', mode="w", encoding="utf-8")
    write_file.write(file_content)

def append_file(file_name, append_content):
    append_file = open(f'{file_name}.txt', mode="a", encoding="utf-8")
    append_file.write(append_content)

def read_file(file_name):
    read_file = open(f'{file_name}.txt', encoding="utf-8")
    return read_file.read()
