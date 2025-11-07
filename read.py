import csv

def read_csv(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_csv("data.csv")
