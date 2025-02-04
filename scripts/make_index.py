from PyPDF2 import PdfReader
from collections import Counter
import re

# Load the PDF file
pdf_path = "YourPDFFile.pdf"
pdf_reader = PdfReader(pdf_path)
number_of_pages = len(pdf_reader.pages)

# Common words to ignore
common_words = set(["the", "and", "a", "to", "of", "in", "it", "is", "for", "on", "with", "as", "was", "by", "at"])

# Initialize a Counter for terms with their page numbers
term_pages = {}

# Process each page
for i in range(number_of_pages):
    page = pdf_reader.pages[i]
    text = page.extract_text()  # Extract text from the page
    
    # Clean and tokenize the text
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in common_words and len(word) > 3]
    
    # Add terms and their page numbers
    for word in filtered_words:
        if word in term_pages:
            term_pages[word].add(i + 1)  # Add 1 because page numbers start from 1
        else:
            term_pages[word] = {i + 1}

# Write the .idx file
with open("document.idx", "w") as index_file:
    for term, pages in term_pages.items():
        page_list = ",".join(map(str, sorted(pages)))  # Format page numbers as a comma-separated list
        index_file.write(f"\\indexentry{{{term}}}{{{page_list}}}\n")