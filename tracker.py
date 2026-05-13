import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv

def fetch_events(url: str) -> list:
    # This 'User-Agent' tells the server you are using a real browser on a Mac
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        # We add a timeout so it doesn't stay 'stuck' forever
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    events = []
    
    # Assuming the structure of the HTML is known
    # Find the product containers
    event_elements = soup.find_all('div', class_='caption')
    
    for element in event_elements:
        # Find the product title (stored in an <a> tag)
        title_element = element.find('a', class_='title')
        # Find the price (stored in an <h4> tag)
        price_element = element.find('h4', class_='price')
        
        if title_element and price_element:
            event_name = title_element.text.strip()
            # We'll map 'Price' to our 'Date' column for this test
            event_date = price_element.text.strip() 
            # Get the link (it's relative, so we append the base URL)
            link = "https://webscraper.io" + title_element['href']
            
            events.append({
                'Event Name': event_name,
                'Price/Date': event_date,
                'Application Link': link
            })    
    return events

def display_events(events: list):
    """
    Displays the events in a formatted table.
    
    Args:
        events (list): A list of dictionaries, each containing event details.
    """
    headers = events[0].keys()
    rows = [tuple(event.values()) for event in events]
    
    print(tabulate(rows, headers=headers, tablefmt='grid'))

def save_to_csv(events: list, filename: str = 'opportunities.csv'):
    """
    Saves the events to a CSV file.
    
    Args:
        events (list): A list of dictionaries, each containing event details.
        filename (str): The name of the CSV file to save.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=events[0].keys())
        writer.writeheader()
        writer.writerows(events)

def main():
    url = 'https://webscraper.io/test-sites/e-commerce/allinone'
    events = fetch_events(url)
    
    if not events:
        print("No events found.")
        return
    
    display_events(events)
    
    save_choice = input("Do you want to save the results to a CSV file? (y/n): ")
    if save_choice.lower() == 'y':
        save_to_csv(events)
        print(f"Results saved to opportunities.csv")

if __name__ == '__main__':
    main()
