import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv

def fetch_events(url: str) -> list:
    """
    Fetches upcoming events from the provided URL.
    
    Args:
        url (str): The URL of the hackathon page to scrape.
        
    Returns:
        list: A list of dictionaries, each containing event details.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    events = []
    
    # Assuming the structure of the HTML is known
    event_elements = soup.find_all('div', class_='event-item')  # Adjust this selector based on the actual HTML structure
    
    for element in event_elements:
        event_name = element.find('h2').text.strip()
        event_date = element.find('span', class_='date').text.strip()
        application_link = element.find('a')['href']
        
        events.append({
            'Event Name': event_name,
            'Date': event_date,
            'Application Link': application_link
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
    url = 'https://unstop.io/hackathons'  # Replace with the actual URL
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
