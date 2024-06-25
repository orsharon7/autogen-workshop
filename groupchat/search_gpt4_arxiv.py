# filename: search_gpt4_arxiv.py
import requests

# Define the search query and sort by submission date in descending order
search_query = "gpt-4"
url = f"http://export.arxiv.org/api/query?search_query=all:{search_query}&sortBy=submittedDate&sortOrder=descending&max_results=1"

response = requests.get(url)

# Print the response content
print(response.content.decode('utf-8'))