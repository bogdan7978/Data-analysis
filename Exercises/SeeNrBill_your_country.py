"""
For this to work, the file 'Billionaires Statistics Dataset.csv' is needed
In this program you just have to run it, write the name of the country you want
and then it will display the number of billionaires in the chosen country
"""

import csv
from collections import defaultdict

# Input country
input_country = input("Enter a country: ")

# Dictionary to store billionaire counts by country
billionaires_by_country = defaultdict(int)

# Open and read the CSV file
with open('Billionaires Statistics Dataset.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Check if the 'country' column in the CSV row matches the input country
        if row['country'] == input_country:
            # Add to the dictionary
            billionaires_by_country[input_country] += 1

# Display the count of billionaires for the input country
if billionaires_by_country[input_country] > 0:
    print(f"Number of billionaires in {input_country}: {billionaires_by_country[input_country]}")
else:
    print(f"No billionaires found in {input_country}")
