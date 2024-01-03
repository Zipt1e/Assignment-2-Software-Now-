
import csv
import requests
from io import StringIO

# GitHub raw CSV file URLs
csv_file_urls = [
    'https://raw.githubusercontent.com/Zipt1e/Assignment-2-Software-Now-/main/CSV/CSV1.csv',
    'https://raw.githubusercontent.com/Zipt1e/Assignment-2-Software-Now-/main/CSV/CSV2.csv',
    'https://raw.githubusercontent.com/Zipt1e/Assignment-2-Software-Now-/main/CSV/CSV3.csv',
    'https://raw.githubusercontent.com/Zipt1e/Assignment-2-Software-Now-/main/CSV/CSV4.csv'
]

# Initialize an empty list to store all text
all_text = []

# Function to process CSV content from a URL
def process_csv(url):
    response = requests.get(url)
    response.raise_for_status()  # This will raise an error if the download failed
    content = StringIO(response.text)
    reader = csv.reader(content)
    return [" ".join(row) for row in reader]

# Loop through each CSV file URL
for url in csv_file_urls:
    csv_content = process_csv(url)
    all_text.append(f"===== Begin {url} =====\n")
    all_text.append("\n".join(csv_content))
    all_text.append(f"\n===== End {url} =====\n")

# Path to the output text file
output_text_file_path = r'C:\Users\azali\OneDrive\Documents\GITKRAKEN\Assignment-2-Software-Now-\combined_data.txt'

# Write all the text to the output file
with open(output_text_file_path, 'w', encoding='utf-8') as file:
    file.write("\n".join(all_text))

print(f"Data extracted from all CSV files into {output_text_file_path}")

import re
from collections import Counter
import csv

# Path to the text file
text_file_path = r'C:\Users\azali\OneDrive\Documents\GITKRAKEN\Assignment-2-Software-Now-\combined_data.txt'

# Read the text file
with open(text_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Use regular expression to extract words from the text
words = re.findall(r'\w+', text.lower())

# Count the occurrences of each word
word_counts = Counter(words)

# Get the 'Top 30' most common words
top_30_words = word_counts.most_common(30)

# Path to the output CSV file
output_csv_path = r'C:\Users\azali\OneDrive\Documents\GITKRAKEN\Assignment-2-Software-Now-\top_30_words.csv'

# Write the 'Top 30' common words and their counts to a CSV file
with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Word', 'Count'])  # Writing the header
    writer.writerows(top_30_words)

print(f"Top 30 common words and their counts are stored in {output_csv_path}")

import transformers
from collections import Counter

def count_top_tokens(text_path, top_n=30):
    # Initialize the tokenizer
    tokenizer = transformers.AutoTokenizer.from_pretrained("bert-base-uncased")

    # Read the text file
    with open(text_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Count the occurrences of each token
    token_counts = Counter(tokens)

    # Get the top 'n' tokens
    top_tokens = token_counts.most_common(top_n)

    return top_tokens

# Path to the text file
text_file_path = r'C:\Users\azali\OneDrive\Documents\GitHub\HIT137\combined_data.txt'

# Get the top 30 tokens
top_30_tokens = count_top_tokens(text_file_path)

# Display the top 30 tokens
for token, count in top_30_tokens:
    print(f"{token}: {count}")

