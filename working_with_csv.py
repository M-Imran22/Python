import csv

# how to open csv file and write data into it.
# with open("data.csv", "w", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Student_name", "Marks_in_english", "Rol_No"])
#     writer.writerow(["M Imran", 89, 202])
#     writer.writerow(["M nasir", 90, 201])

# read data form csv file.
with open("data.csv", newline='') as file:
    reader = csv.reader(file)

# print the data in list of list (each row convert into a list)
print(list(reader))

# print each row of csv file
for row in reader:
    print(row)
