"""
For this to work, the file 'Billionaires Statistics Dataset.csv' is needed
In this program you just have to run it, write the name of the country you want
and then it will create an CSV file, that you can open with Excel, 
where it will be displayed the billionaires in the chosen country and a lot of data about them
"""

import csv


input_country = input("Enter a country: ")

# Create a list to store the matching rows
match_billionaires = []

# Open and read the CSV file
with open('Billionaires Statistics Dataset.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        # Check if the 'country' column in the CSV row matches the input country
        if row['country'] == input_country:
            match_billionaires.append(row)

if not match_billionaires:
    print(f"No billionaires found in {input_country}")
else:
    # Write the matching rows to a new CSV file
    output_filename = f'{input_country}_billionaires.csv'
    with open(output_filename, mode='w', newline='') as output_file:
        fieldnames = match_billionaires[0].keys()
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(match_billionaires)

    print(f"{len(match_billionaires)} billionaires found in {input_country}.")
    print(f"Data has been saved to {output_filename}")
