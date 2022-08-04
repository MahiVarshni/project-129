import csv
dataset_1=[]
dataset_2=[]

with open("final.csv","r")as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)


with open("dwarf_stars_clea2.csv","r")as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)

header_1=dataset_1[0]
star_data_1=dataset_1[1:]

header_2=dataset_2[0]
star_data_2=dataset_2[1:]

headers=header_1+header_2
star_data=[]

for index,data_row in enumerate(star_data_1):
    star_data.append(star_data_1[index]+star_data_2[index])

#creating csv files
with open("merged.csv","a+")as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)

#remove blank lines
with open("merged.csv")as input,open("merged2.csv","w",newline="")as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)