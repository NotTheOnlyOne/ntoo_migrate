from datetime import datetime, timedelta

# Get today's date
today = datetime.now()
target = 10000

# Get the end of the year
end_of_year = datetime(today.year, 12, 31)

# Calculate the difference
days_until_end_of_year = (end_of_year - today).days

num_items = int(input("Enter the number of items: "))
print("Number of items entered:", num_items)

print("Days until the end of the year:", days_until_end_of_year)

items_per_day = (target - num_items)/days_until_end_of_year

print(items_per_day)

