import os
import re

character_lines = []

def strip_parentheses(s):
    return re.sub(r'\(.*?\)', '', s)
    
def is_single_word_all_caps(s):
    # First, we split the string into words
    words = s.split()

    # Check if the string contains only a single word
    if len(words) != 1:
        return False

    # Check if the single word is in all caps
    return words[0].isupper()
    
def process_directory(directory_path, character_name):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):  # Ignore directories
            extract_character_lines(file_path, character_name)
            
    with open(f'./{character_name}_lines.jsonl', 'w', newline='') as outfile:
        prevLine = ''
        for s in character_lines:
            if (s.startswith('DATA:')):
                outfile.write("{\"prompt\": \"" + prevLine + "###\", \"completion\": \" " + s + "END\"}\n")
            prevLine = s

def extract_character_lines(file_path, character_name):
    with open(file_path, 'r') as script_file:
        lines = script_file.readlines()

    is_character_line = False
    current_line = ''
    current_character = ''
    for line in lines:
        strippedLine = line.strip()
        if (is_single_word_all_caps(strippedLine)):
            is_character_line = True
            current_character = strippedLine
        elif (line.strip() == '') and is_character_line:
            is_character_line = False
            dialog_line = strip_parentheses(current_line).strip()
            dialog_line = dialog_line.replace('"', "'")
            character_lines.append(current_character + ": " + dialog_line)
            current_line = ''
        elif is_character_line:
            current_line += line.strip() + ' '

process_directory('e:/Downloads23/scripts_tng', 'DATA')
