import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send an HTTP request with headers
url = 'https://www.bbc.com/news'  # Replace with a simpler target URL for testing
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract specific information (e.g., all paragraphs)
headings = soup.find_all('p')  # Example.com uses <p> tags for paragraphs

# Step 4: Save the data to a CSV file
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Paragraph'])  # Write header
    for heading in headings:
        writer.writerow([heading.text.strip()])  # Write each paragraph text

print("Data has been scraped and saved to data.csv")
