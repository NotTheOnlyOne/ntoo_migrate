
import requests
from bs4 import BeautifulSoup

def get_url(url):

    url = url.replace("\n", "")

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the title tag and get its text
        title = soup.title.text.strip()
        
        # Print the title
        print("Title:", title)
        print("URL:", url)
        
        # Print the HTML content
        #print("HTML Content:")
        #print(response.text)
    else:
        print("Failed to retrieve HTML content. Status code:", response.status_code, url)
    

def read_tsv_file(filename):
    
    no_title = 0
    snapshot = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the line by tabs

                data = line.split('\t')
                timestamp = data[0]
                title = data[1]
                details = data[2]
                link = data[3]

                if title == "" and details =="":
                    no_title = no_title + 1
                if title == "Snapshot":
                    snapshot = snapshot + 1
                    print(data)
                    get_url(link)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    #except Exception as e:
    #    print(f"An error occurred: {e}")

    print("No title "+str(no_title))
    print("Snapshot "+str(snapshot))

# Replace 'ntoo.tsv' with the appropriate file path if the file is not in the same directory as the script
read_tsv_file('ntoo.tsv')

