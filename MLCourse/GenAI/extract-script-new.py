import os
import re
import random
character_lines = []

def strip_parentheses(s):
    return re.sub(r'\(.*?\)', '', s)
    
def is_single_word_all_caps(s):
    # First, we split the string into words
    words = s.split()

    # Check if the string contains only a single word
    if len(words) != 1:
        return False

    # Make sure it isn't a line number
    if bool(re.search(r'\d', words[0])):
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
                outfile.write("{\"messages\": [{\"role\": \"system\", \"content\": \"Data is an android in the TV series Star Trek: The Next Generation.\"}, {\"role\": \"user\", \"content\": \"" + prevLine + "\"}, {\"role\": \"assistant\", \"content\": \"" + s + "\"}]}\n")
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
            
def split_file(input_filename, train_filename, eval_filename, split_ratio=0.8, max_lines=10000):
    """
    Splits the lines of the input file into training and evaluation files.

    :param input_filename: Name of the input file to be split.
    :param train_filename: Name of the output training file.
    :param eval_filename: Name of the output evaluation file.
    :param split_ratio: Ratio of lines to be allocated to training. Default is 0.8, i.e., 80%.
    """
    
    with open(input_filename, 'r') as infile:
        lines = infile.readlines()

    # Shuffle lines to ensure randomness
    random.shuffle(lines)
    
    lines = lines[:max_lines]

    # Calculate the number of lines for training
    train_len = int(split_ratio * len(lines))

    # Split the lines
    train_lines = lines[:train_len]
    eval_lines = lines[train_len:]

    # Write to the respective files
    with open(train_filename, 'w') as trainfile:
        trainfile.writelines(train_lines)

    with open(eval_filename, 'w') as evalfile:
        evalfile.writelines(eval_lines)

process_directory('e:/Downloads23/scripts_tng', 'DATA')
split_file('./DATA_lines.jsonl', './DATA_train.jsonl', './DATA_eval.jsonl')
