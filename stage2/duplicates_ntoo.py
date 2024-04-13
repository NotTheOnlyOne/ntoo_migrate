
import requests
from bs4 import BeautifulSoup

def read_tsv_file(filename):
    
    no_title = 0
    snapshot = 0
    duplicate_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the line by tabs

                data = line.split('\t')
                timestamp = data[0]
                title = data[1]
                details = data[2]
                link = data[3].lower()

                if link not in duplicate_dict:
                    duplicate_dict[link] = {}

                if title not in duplicate_dict[link]:
                    duplicate_dict[link][title] = 1
                else:
                    duplicate_dict[link][title] += 1
                
                if title == "Snapshot":
                    snapshot = snapshot + 1


        snapshot_to_delete = 0
        for link in duplicate_dict:
            link_dict = duplicate_dict[link]
            if len(link_dict) > 1 and 'Snapshot' in link_dict:
                snapshot_to_delete += 1
                print(link_dict)
                print(link)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    #except Exception as e:
    #    print(f"An error occurred: {e}")

    print("Snapshot "+str(snapshot))
    print("Snapshot to delete "+str(snapshot_to_delete))

# Replace 'ntoo.tsv' with the appropriate file path if the file is not in the same directory as the script
read_tsv_file('database_ntoo.tsv')

