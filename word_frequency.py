import csv
import os
import re
from collections import Counter
import sqlite3


# Define common words to ignore
STOP_WORDS = {"a", "an", "the", "and", "or", "but", "is", "in", "of", "to", "for", "on", "with", "as", "was", "were", "has", 
              "have", "at", "by", "their", "which", "that", "this", "those", "be", "i", "it", "not", "he", "she", "we", "me", 
              "him", "her", "el", "la", "los", "las", "un", "una", "para", "se", "de", "y", "que", "en", "lo", "esta", "fue", 
              "son", "con", "un", "una", "del", "la", "al"}


def count_word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    words = [word for word in words if word not in STOP_WORDS and not word.isdigit()]
    word_freq = Counter(words)
    return word_freq


def process_csv_file(file_path, output_folder):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            id_, source, original_text = row
            word_freq = count_word_frequency(original_text)
            print(word_freq)
            store_word_frequency_in_database(id_, source, word_freq)
    move_processed_csv(file_path, output_folder)


def store_word_frequency_in_database(id_, source, word_freq):
    conn = sqlite3.connect('word_frequency.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS word_frequency
                 (id INTEGER PRIMARY KEY, source TEXT, word TEXT, frequency INTEGER)''')
    for word, freq in word_freq.items():
        c.execute("INSERT INTO word_frequency (id, source, word, frequency) VALUES (?, ?, ?, ?)",
                  (id_, source, word, freq))
    conn.commit()
    conn.close()


def move_processed_csv(file_path, output_folder):
    file_name = os.path.basename(file_path)
    output_file_path = os.path.join(output_folder, file_name)
    os.rename(file_path, output_file_path)


# Main function
def main(input_folder, output_folder):
    
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist. Please provide a valid input folder path.")
        return

    if not os.path.exists(output_folder):
        print(f"Output folder '{output_folder}' does not exist. Please provide a valid output folder path.")
        return
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_folder, file_name)
            process_csv_file(file_path, output_folder)


if __name__ == "__main__":
    input_folder = "<path_to_input_folder>"
    output_folder = "path_to_output_folder"
    main(input_folder, output_folder)

