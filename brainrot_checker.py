import os
import re
import pyfiglet
import random
from termcolor import colored

# Define a list of colors
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def load_brainrot_phrases(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def check_brainrot(text, brainrot_phrases):
    text = text.lower()
    found_phrases = [phrase for phrase in brainrot_phrases if re.search(re.escape(phrase.lower()), text)]
    return found_phrases

def calculate_percentage(brainrot_count, total_words):
    return (brainrot_count / total_words) * 100 if total_words > 0 else 0

def print_multicolored_ascii_text(text):
    ascii_art = pyfiglet.figlet_format(text)
    multicolored_output = ''.join(
        colored(char, random.choice(COLORS)) if char != '\n' else '\n' for char in ascii_art
    )
    print(multicolored_output)

if __name__ == "__main__":
    clear_terminal()  # Clear the terminal at the start
    print_multicolored_ascii_text("Brainrot Checker")
    print("By 0M3REXE")
    
    brainrot_phrases = load_brainrot_phrases('brainrot_phrases.txt')

    while True:
        input_text = input("\nEnter a phrase to check for Brainrot (or type 'exit' to quit): ")
        
        if input_text.lower() == 'exit':
            print("Exiting the Brainrot Checker. Goodbye!")
            break

        found_phrases = check_brainrot(input_text, brainrot_phrases)
        total_words = len(input_text.split())
        brainrot_count = len(found_phrases)
        percentage = calculate_percentage(brainrot_count, total_words)

        if brainrot_count > 0:
            print(f"Brainrot Level: {brainrot_count} (This text has {brainrot_count} Brainrot phrases: {', '.join(found_phrases)})")
            print(f"Percentage of Brainrot: {percentage:.2f}%")
        else:
            print("Brainrot Level: 0 (You are Normal)")
