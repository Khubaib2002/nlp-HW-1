import re

def read(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # tokens = re.split(r'\s+', content)       was thinking whether this would be applicable too
    tokens = re.findall(r'[\u0600-\u06FF]+', content)
    return tokens

def write(tokens, file_dest):
    with open(file_dest, 'w', encoding='utf-8') as file:
        for token in tokens:
            file.write(token + '\n')

file_path = "urdu_text_input.txt"
tokens = read(file_path)
write(tokens, "urdu_output.txt")
print("DONE")