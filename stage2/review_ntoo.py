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
                    print(data)
                if title == "Snapshot":
                    snapshot = snapshot + 1
                    print(data)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    #except Exception as e:
    #    print(f"An error occurred: {e}")

    print("No title "+str(no_title))
    print("Snapshot "+str(snapshot))

# Replace 'ntoo.tsv' with the appropriate file path if the file is not in the same directory as the script
read_tsv_file('ntoo.tsv')

