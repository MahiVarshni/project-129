
#cleaning the  file

import csv
dataset_1=[]


with open("dwarf_stars.csv","r")as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)

headers=dataset_1[0]
star_data=dataset_1[1:]

#converting all star names to lower case
for data in star_data:
    data[2]=data[2].lower()

#sorting stars in alphabetical order
star_data.sort(key=lambda star_data:star_data[2])

#creating csv files
with open("dwarf_stars_clea1.csv","a+")as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)

#remove blank lines
with open("dwarf_stars_clea1.csv")as input,open("dwarf_stars_clea2.csv","w",newline="")as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
