from scholarly import scholarly

# Replace with your bibliographic data in natural language
references = [
    "Doe, J., et al. A Great Paper, Journal of Awesome Science, 2023",
    "Smith, A. An Amazing Article, Another Journal, 2021"
]

for ref in references:
    search_query = scholarly.search_pubs(ref)
    try:
        pub = next(search_query)
        bibtex = pub.bibtex  # Fetch BibTeX data
        print(bibtex)
    except StopIteration:
        print(f"No results for: {ref}")