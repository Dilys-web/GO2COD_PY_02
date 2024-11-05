 # Web Scraper in Python

## Overview
This project demonstrates how to create a simple web scraper using Python. The scraper is designed to fetch and parse specific information from a webpage, such as headlines and prices. By utilizing the `requests` and `BeautifulSoup` libraries, you can easily extract data from HTML content.

## Features
- Fetch webpage content using HTTP requests.
- Parse HTML to extract specific information like headlines and prices.
- Use Python libraries to simplify the web scraping process.

## Requirements
To run this project, you need:
- Python 3.x
- `requests` library (for making HTTP requests)
- `BeautifulSoup` (for parsing HTML)

### Installation
1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required libraries using pip:
   ```bash
   pip install requests beautifulsoup4
   ```

### How It Works

**Fetch the Webpage Content:** The requests.get() function is used to download the HTML content of the specified URL.

**Parse the HTML:** The BeautifulSoup library is used to parse the HTML content.

### Extract Data:
Use find_all() to locate specific HTML tags (e.g., h2 for headlines).
Use find_all(class_='price') to extract elements with a specific class for prices.
Display the Data: The extracted headlines and prices are printed to the console.

### Usage
Clone or download this repository to your local machine.

Run the script using Python:
```bash

python web_scraper.py
```
Enter the URL of the webpage you wish to scrape when prompted.
The program will display the extracted headlines and prices.

### Customization
You can customize the scraper to target different HTML tags and classes based on the structure of the webpage you are scraping. Modify the find_all() methods to match the desired elements.   

### License
This project is open-source and available for modification and distribution. You are welcome to contribute!