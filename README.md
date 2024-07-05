# Travel Agencies Scraper

## Overview

This project is a web scraper built with Scrapy to extract travel agency details from the Lufthansa City Center website. The scraper navigates through the website's alphabetical pages (from A to Z) and collects information such as the name, address, phone number, and email of each travel agency. The collected data is then saved into a text file [travel_agencies.txt](https://github.com/user-attachments/files/16112312/travel_agencies.txt)


## Features
- **Alphabetical Pagination**: The scraper navigates through pages for each letter from A to Z.
- **Data Extraction**: Extracts agency name, address, phone number, and email.
- **File Output**: Saves the extracted data into a structured text file.


## Usage
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/lufthansa-scraper.git
   cd lufthansa-scraper
2. **Install Scrapy**:
   pip install scrapy
3. **Run script**:
   scrapy runspider lufthansa_spider.py
4. The extracted data will be saved to travel_agencies/travel_agencies.txt


## Pagination - Handling Secondary Links (the challenge)
The Lufthansa City Center website organizes its travel agencies alphabetically, each letter corresponding to a different page. To handle this pagination, the scraper:

1. Dynamic URL Generation: Constructs URLs for each alphabetical page (from A to Z) using a base URL template.
2. Iterative Requests: Initiates requests for each generated URL to scrape the respective pages.
3. Sequential Processing: Processes each page sequentially, extracting the necessary details before moving to the next page.
   
def start_requests(self):
    base_url = 'https://lufthansa-city-center.com/en/our-travel-agencies/from-a-to-z/?city={}'
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    start_urls = [base_url.format(letter) for letter in letters]
    for url in start_urls:
        yield scrapy.Request(url, callback=self.parse)

## Future Improvements
1. Error Handling: Enhance error handling to manage network issues or unexpected HTML structure changes.
2. Data Storage: Optionally store the data in other formats (e.g., CSV, XLS) or directly into a database.

