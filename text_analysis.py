
import os
# Define project path
PROJECT_PATH = "/Test Assignment"
os.chdir(PROJECT_PATH)

# Import and Install Required Libraries
 !pip install requests beautifulsoup4 nltk pandas openpyxl

import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import re

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Load Input Data
df = pd.read_excel('Input.xlsx')

# Create a Directory for Extracted Text
TEXT_DIR = os.path.join(PROJECT_PATH, "TitleText")
os.makedirs(TEXT_DIR, exist_ok=True)

# Extract and Save Text from URLs
HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

for index, row in df.iterrows():
    url, url_id = row['URL'], row['URL_ID']
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('h1').get_text() if soup.find('h1') else "No Title"
        article = " ".join([p.get_text() for p in soup.find_all('p')])

        with open(os.path.join(TEXT_DIR, f"{url_id}.txt"), 'w', encoding='utf-8') as file:
            file.write(title + '\n' + article)
    except Exception as e:
        print(f"Error processing {url_id}: {e}")

# Load Stop Words
STOPWORDS_DIR = os.path.join(PROJECT_PATH, "StopWords")
stop_words = set()
for file in os.listdir(STOPWORDS_DIR):
    with open(os.path.join(STOPWORDS_DIR, file), 'r', encoding='ISO-8859-1') as f:
        stop_words.update(f.read().splitlines())

# Tokenize and Clean Extracted Text
docs = []
for text_file in os.listdir(TEXT_DIR):
    with open(os.path.join(TEXT_DIR, text_file), 'r', encoding='utf-8') as f:
        words = word_tokenize(f.read())
        filtered_words = [word for word in words if word.lower() not in stop_words]
        docs.append(filtered_words)

# Load Positive and Negative Word Dictionaries
SENTIMENT_DIR = os.path.join(PROJECT_PATH, "MasterDictionary")
pos_words, neg_words = set(), set()
for file in os.listdir(SENTIMENT_DIR):
    with open(os.path.join(SENTIMENT_DIR, file), 'r', encoding='ISO-8859-1') as f:
        (pos_words if 'positive' in file else neg_words).update(f.read().splitlines())

# Perform Sentiment Analysis
positive_score = []
negative_score = []
polarity_score = []
subjectivity_score = []
for doc in docs:
    pos_count = sum(1 for word in doc if word.lower() in pos_words)
    neg_count = sum(1 for word in doc if word.lower() in neg_words)
    positive_score.append(pos_count)
    negative_score.append(neg_count)
    polarity_score.append((pos_count - neg_count) / ((pos_count + neg_count) + 0.000001))
    subjectivity_score.append((pos_count + neg_count) / (len(doc) + 0.000001))

Compute Readability Metrics
def compute_readability(file):
    with open(os.path.join(TEXT_DIR, file), 'r', encoding='utf-8') as f:
        text = f.read()
        # Clean text keeping sentence terminators
        text = re.sub(r'[^\w\s.!?]', '', text)
        # Split sentences using multiple delimiters
        sentences = [s.strip() for s in re.split(r'[.!?]', text) if s.strip()]
        num_sentences = len(sentences)

        # Process words with combined functionality
        words = []
        total_letters = 0
        for word in text.split():
            # Clean and normalize the word
            cleaned_word = re.sub(r'[^a-zA-Z]', '', word).lower()
            if cleaned_word and cleaned_word not in stop_words:
                words.append(cleaned_word)
                total_letters += len(cleaned_word)  # Count letters

        num_words = len(words)

        # Handle edge cases with zero division
        if num_sentences == 0 or num_words == 0:
            return (0.0, 0.0, 0.0, 0.0, 0, 0.0)

        # Calculate syllables and complex words
        complex_words = []
        syllable_count = 0
        for word in words:
            # Count vowels (syllables approximation)
            vowels = sum(1 for c in word if c in 'aeiou')
            # Handle es/ed endings
            if word.endswith(('es', 'ed')) and vowels > 1:
                vowels -= 1
            syllable_count += vowels
            if vowels > 2:
                complex_words.append(word)

        # Calculate all metrics
        avg_words_per_sentence = num_words / num_sentences
        avg_letters_per_sentence = total_letters / num_sentences
        complex_count = len(complex_words)
        percent_complex = (complex_count / num_words) * 100
        fog_index = 0.4 * (avg_words_per_sentence + percent_complex)
        syllable_per_word = syllable_count / num_words

        return (
            avg_words_per_sentence,
            avg_letters_per_sentence,
            percent_complex,
            fog_index,
            complex_count,
            syllable_per_word
        )

# structure
metrics = [compute_readability(file) for file in os.listdir(TEXT_DIR)]
avg_words_per_sentence, avg_letters_per_sentence, percent_complex_words, fog_index, complex_word_count, syllable_count_per_word = zip(*metrics)

#Compute Word Count and Average Word Length
def compute_word_metrics(file):
    with open(os.path.join(TEXT_DIR, file), 'r', encoding='utf-8') as f:
        words = [word for word in re.sub(r'[^\w\s]', '', f.read()).split() if word.lower() not in stop_words]
        return len(words), sum(len(word) for word in words) / len(words)

word_count, avg_word_length = zip(*[compute_word_metrics(file) for file in os.listdir(TEXT_DIR)])

# Count Personal Pronouns
def count_pronouns(file):
    with open(os.path.join(TEXT_DIR, file), 'r', encoding='utf-8') as f:
        text = f.read()
        return sum(len(re.findall(r"\b" + pronoun + r"\b", text)) for pronoun in ["I", "we", "my", "ours", "us"])
personal_pronoun_count = [count_pronouns(file) for file in os.listdir(TEXT_DIR)]

# Save Results to Excel
# Load Output Data Structure
output_df = pd.read_excel('Output Data Structure.xlsx')

# Define the variables with corrected mappings
variables = {
    "POSITIVE SCORE": positive_score,
    "NEGATIVE SCORE": negative_score,
    "POLARITY SCORE": polarity_score,
    "SUBJECTIVITY SCORE": subjectivity_score,
    "AVG SENTENCE LENGTH": avg_letters_per_sentence,
    "PERCENTAGE OF COMPLEX WORDS": percent_complex_words,
    "FOG INDEX": fog_index,
    "AVG NUMBER OF WORDS PER SENTENCE": avg_words_per_sentence,
    "COMPLEX WORD COUNT": complex_word_count,
    "WORD COUNT": word_count,
    "SYLLABLE PER WORD": syllable_count_per_word,
    "PERSONAL PRONOUNS": personal_pronoun_count,
    "AVG WORD LENGTH": avg_word_length
}



# Update DataFrame columns
for col_name, values in variables.items():
    output_df[col_name] = list(values)

# Save with proper formatting
output_df.to_excel('Final_Output_Data.xlsx', index=False, float_format="%.3f")
print("✅ Data successfully saved to 'Final_Output_Data.xlsx'!")