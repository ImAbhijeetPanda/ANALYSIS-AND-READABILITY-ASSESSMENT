# Text Analysis and Readability Assessment

The goal of this project is to extract text data from given URLs and perform text analysis, computing various sentiment and readability metrics. The extracted data is processed to generate insights into sentiment polarity, readability, and linguistic complexity.

The script processes URLs from `Input.xlsx` to extract article text and compute sentiment scores (Positive Score, Negative Score, Polarity Score, Subjectivity Score) and readability metrics (Fog Index, Average Sentence Length, Percentage of Complex Words, Complex Word Count, Word Count, Syllable Count Per Word, Personal Pronouns Count, and Average Word Length). The steps involved include scraping article text using `requests` and `BeautifulSoup`, ensuring only the article body and title are extracted. The extracted text is then cleaned by removing stopwords stored in the `StopWords/` directory. Sentiment and readability metrics are computed using the word lists in `MasterDictionary/`, and the results are saved in `Final_Output_Data.xlsx`.

## How to Run the Script

Ensure Python 3.6+ is installed. Install dependencies using:

```bash
pip install requests beautifulsoup4 nltk pandas openpyxl
```

Run the script by navigating to the project folder and executing:

```bash
python text_analysis.py
```

Results will be saved in `Final_Output_Data.xlsx`.

## Explanation of Steps

1. **Extracting Text from URLs**: 
   - The script reads `Input.xlsx`, which contains a list of URLs.
   - It fetches the content of each URL using the `requests` library and extracts only the article title and body using `BeautifulSoup`.
   - The extracted text is saved as a separate file named with the `URL_ID`.

2. **Cleaning the Text**:
   - Stopwords are removed using predefined lists stored in the `StopWords/` directory.
   - Punctuation and special characters are eliminated to ensure accurate analysis.

3. **Performing Sentiment Analysis**:
   - **Positive Score**: Counts words found in the positive word list.
   - **Negative Score**: Counts words found in the negative word list and converts the count into a positive number.
   - **Polarity Score**: Measures the positivity or negativity of the text using:
     ```
     Polarity Score = (Positive Score – Negative Score) / ((Positive Score + Negative Score) + 0.000001)
     ```
     The score ranges from -1 (completely negative) to +1 (completely positive).
   - **Subjectivity Score**: Determines how much of the text expresses personal opinions, calculated as:
     ```
     Subjectivity Score = (Positive Score + Negative Score) / ((Total Words after cleaning) + 0.000001)
     ```
     The score ranges from 0 (completely objective) to 1 (highly subjective).

4. **Readability Analysis**:
   - **AVG NUMBER OF WORDS PER SENTENCE**: Computed as:
     ```
     AVG NUMBER OF WORDS PER SENTENCE = Total Words / Total Sentences
     ```
   - **Percentage of Complex Words**: Measures the proportion of words with more than two syllables.
   - **Fog Index**: Calculates readability using:
     ```
     Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex Words)
     ```
   - **Complex Word Count**: The total count of words containing more than two syllables.
   - **Word Count**: The total number of words in the cleaned text, excluding stopwords.
   - **Syllable Count Per Word**: Determines the number of vowels in each word and accounts for special cases where endings like "es" or "ed" should not be counted as extra syllables.
   - **Personal Pronouns Count**: Uses regex to count occurrences of pronouns such as "I," "we," "my," "ours," and "us." Ensures that "US" (United States) is not counted mistakenly.
   - **Average Word Length**: Computed as:
     ```
     Average Word Length = Sum of Characters in Words / Total Word Count
     ```

## Project Structure

```
Text_Analysis_Project/
├── StopWords/               # Contains stopword lists
├── MasterDictionary/        # Contains positive/negative word lists
├── Input.xlsx               # List of URLs for extraction
├── Output Data Structure.xlsx # Template for output format
├── text_analysis.py         # Python script for extraction and analysis
└── Final_Output_Data.xlsx   # Processed output data
```

## Dependencies

Python Libraries: `requests`, `beautifulsoup4`, `nltk`, `pandas`, `openpyxl`  
NLTK Datasets (auto-downloaded by the script): `punkt`, `stopwords`

## Notes

Ensure URLs in `Input.xlsx` are publicly accessible. Folder names (`StopWords/`, `MasterDictionary/`) **must** match exactly. Adjust `PROJECT_PATH` in `text_analysis.py` if your folder structure differs.

---
## 🏆 Contributors   
👤 **Abhijeet Panda** (LinkedIn: [Abhijeet's Profile](https://www.linkedin.com/in/imabhijeetpanda))  

---
## 🎉 Acknowledgments  
Special thanks to:   
- **Google Colab** for providing training resources.

---
## 🔗 Repository Link  
🔗 [GitHub Repository](https://github.com/ImAbhijeetPanda/Text-Analysis-and-Readability-Assessment)

For any questions or feedback, feel free to reach out:

- **Email**: [iamabhijeetpanda@gmail.com](mailto:iamabhijeetpanda@gmail.com)
- **LinkedIn**: [Abhijeet Panda](https://www.linkedin.com/in/imabhijeetpanda)
- **GitHub**: [ImAbhijeetPanda](https://github.com/ImAbhijeetPanda)



🚀 **Feel free to fork, contribute, or raise an issue!** 😃

