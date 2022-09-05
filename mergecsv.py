import csv

def merge_csv(csv_list, ouyput_path):
    fieldnames = list()
    for filr in csv_list:
        with open(file, 'r') as input_csv:
            fn = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(x for x in fn if x not in fieldnames)

with open(output_path, 'w', newline=' ') as output.csv:
    writer = csv.DictWriter(output_csv, fieldnames = fieldnames)
    writer.writeheader()
    for file in csv_list:
        with open(file,'r') as input.csv:
            reader =csv.DictReader(input_csv)
            for row in reader:
                writer.writerow(row)