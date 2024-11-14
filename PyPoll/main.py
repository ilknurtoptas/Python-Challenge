import os
import csv

# Set the path for the CSV file
csvpath = os.path.join("Resources","election_data.csv")

print(f"Attempting to open: {csvpath}")

with open(csvpath, encoding= "UTF-8") as csvfile:

  #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

print("checking")
