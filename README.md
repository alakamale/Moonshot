# Moonshot Word Frequency Analysis

This Python script performs word frequency analysis on text data stored in CSV files. It counts the frequency of each word in the "original_text" segment of the CSV files, ignoring common words, numeric values, and emojis. The results are stored in a SQLite database along with the original fields from the CSV files.

## Requirements

- Python 3.x
- SQLite3 (for storing word frequency data)
- CSV files with the specified structure (see sample CSV structure below)

## Usage

1. Clone or download the repository to your local machine.
2. Ensure Python and SQLite3 are installed on your machine.
3. Place the CSV files containing text data in the `input_folder` directory.
4. Open the Python script (`word_frequency.py`) in a text editor.
5. Update the `input_folder` and `output_folder` paths in the script to match the directory paths on your machine. These paths specify the location of input CSV files and where processed files will be moved.
6. Save the changes to the Python script.
7. Open a terminal or command prompt and navigate to the directory containing the Python script (`word_frequency.py`).
8. Run the script using the following command:
   ```
   python word_frequency.py
   ```
9. The script will process the CSV files in the specified `input_folder`, perform word frequency analysis, store the results in a SQLite database (`word_frequency.db`), and move the processed CSV files to the specified `output_folder`.

## Sample CSV Structure

The input CSV files should have the following structure:

```
"id", "source", "original_text"
1001234, "OnlineSource1", "Text data here..."
1001235, "OnlineSource2", "Text data here..."
1001236, "OnlineSource2", "Text data here..."
```

- The `original_text` segment contains the text data for word frequency analysis.

## Customize

- Modify the `common_words` set in the Python script to add or remove common words to ignore during word frequency analysis.
- Customize the `input_folder` and `output_folder` paths in the script according to your directory structure.

## Notes

- Ensure that the CSV files are properly formatted and contain text data in the specified segments.
- The script will create a SQLite database file (`word_frequency.db`) in the same directory as the Python script to store the word frequency data.

```
