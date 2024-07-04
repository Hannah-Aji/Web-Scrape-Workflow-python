import scrapy

class LufthansaSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['lufthansa-city-center.com']

    def start_requests(self):
        # Define the base URL for the alphabet pages
        base_url = 'https://lufthansa-city-center.com/en/our-travel-agencies/from-a-to-z/?city={}'

        # List of letters from A to Z
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # Generate start URLs for each letter
        start_urls = [base_url.format(letter) for letter in letters]

        # Start requests for each URL
        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # Select the column with 'h2' containing 'Travel Agencies'
        columns = response.css('div.column')
        for column in columns:
            title = column.css('h2.glossary-title::text').get()
            if title and 'Travel Agencies' in title:
                # Extract travel agency links from the selected column
                agency_items = column.css('ul li')
                for item in agency_items:
                    name = item.css('a::text').get()
                    link = item.css('a::attr(href)').get()
                    if name and link:
                        # Follow the link to the agency's page and pass the name to the callback
                        yield response.follow(link, self.parse_agency, cb_kwargs={'name': name.strip()})

    def parse_agency(self, response, name):
        # Extract the travel agency details from the individual page
        
        # Extracting address
        address_lines = response.css('div.address__street::text').getall()
        address = ' '.join([line.strip().replace('\n', ' ') for line in address_lines if line.strip()])

        # Extracting phone number
        phone = response.css('div.details-agency a[href^="tel:"]::text').get()
        
        # Extracting email address
        email = response.css('div.details-agency a[href^="mailto:"]::text').get()

        # Format the output as per the specified format
        output = f"Name: {name}\nAddress: {address}\nPhone: {phone}\nEmail: {email}\n\n"

        # Write to a .txt file
        with open('travel_agencies/travel_agencies.txt', 'a', encoding='utf-8') as f:
            f.write(output)

    
