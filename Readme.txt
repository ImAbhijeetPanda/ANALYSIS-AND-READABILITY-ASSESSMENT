TEXT ANALYSIS PROJECT README

====================================
1. SOLUTION APPROACH
====================================
- The script processes URLs from Input.xlsx to extract article text and compute:
  1. Sentiment scores (Positive, Negative, Polarity, Subjectivity)
  2. Readability metrics (Fog Index, Avg Word Length, etc.)
- Steps:
  a) Scrape titles and paragraphs using requests and BeautifulSoup.
  b) Clean text by removing stopwords (from StopWords/ directory).
  c) Calculate scores using MasterDictionary/ word lists.
  d) Save results to Final_Output_Data.xlsx.

====================================
2. HOW TO RUN THE SCRIPT
====================================
Prerequisites:
- Python 3.6+ installed
- Required libraries (install via command below)

Steps:
1. Set up folder structure:
   Project_Folder/
   ├── StopWords/           # Contains all stopword text files
   ├── MasterDictionary/    # Contains positive/negative word lists
   ├── Input.xlsx           # Input URLs (columns: URL_ID, URL)
   ├── Output Data Structure.xlsx  # Template for output
   └── text_analysis.py     # The Python script

2. Install dependencies:
   Open terminal and run:
   pip install requests beautifulsoup4 nltk pandas openpyxl

3. Run the script:
   Navigate to the project folder in terminal and execute:
   python text_analysis.py

4. Output:
   Results will be saved to Final_Output_Data.xlsx.

====================================
3. DEPENDENCIES
====================================
- Libraries:
  requests, beautifulsoup4, nltk, pandas, openpyxl
- NLTK Datasets (auto-downloaded by the script):
  punkt, stopwords

====================================
NOTES
====================================
- Ensure URLs in Input.xlsx are publicly accessible.
- Folder names (StopWords/, MasterDictionary/) MUST match exactly.
- Adjust PROJECT_PATH in text_analysis.py if your folder structure differs.