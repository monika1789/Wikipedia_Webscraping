import requests
from bs4 import BeautifulSoup
import csv 

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
   

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html5lib')
        # To view the data
        # with open("soup_data.txt", "w", encoding="utf-8") as file:
        #     file.write(str(soup.prettify()))        
        
        # Extract data from the parsed HTML
        div = soup.find('td', class_='navbox-list')
        
        if div:
            nested_ul = div.find('ul')
            print(nested_ul)
            
            if nested_ul:
                filename = 'National_parks.csv'
                with open(filename, 'w', newline='') as f: 
                    # Define fieldnames for the CSV
                    fieldnames = ['link_URL', 'Park_name']
                    # Create a CSV DictWriter object
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    # Write the header row
                    writer.writeheader()
                    # Find all list items within the nested li
                    list_items = nested_ul.find_all('li')
                    print(list_items)
                    # Write data to the CSV file
                    for item in list_items:
                        link = item.find('a')
                        if link:
                            link_url = link.get('href')
                            name = link.get('title')
                        # Write a row to the CSV file
                        writer.writerow({'link_URL': link_url, 'Park_name': name})     
    else:        
        print("Failed to fetch the web page") 
                    
        
def main():        
    url = 'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'
        
    # Call the function to scrape the website
    scrape_website(url)        
    
if __name__ == '__main__': 
    main()