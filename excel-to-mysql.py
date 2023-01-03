import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("reg_table.xls")
# Establish a MySQL connection
sheet = book.sheet_by_name("Registered")
# Using index
#sheet = book.sheet_by_index(0)
# sheet = book.sheet_by_name("Registered")

database = pymysql.connect(host="localhost", user="root", passwd="Seealpsee9302@?$", db="Students")
# Get the cursor, which is used to traverse the db line by line
cursor = database.cursor()
# Create Table called "reg_table"

# Create the INSERT INTO SQL query
query = """INSERT INTO reg_table (ID, name, Class, Section, Registered, Reg_Date) VALUES (%s, %s, %s, %s, %s, %s)"""

# Create a for loop to iterate through each row in the .xls file,
# starting at row 2 to skip the headers"""
for r in range(1, sheet.nrows):
    ID = sheet.cell(r, 0).value
    name = sheet.cell(r, 1).value
    Class = sheet.cell(r, 2).value
    Section = sheet.cell(r, 3).value
    Registered = sheet.cell(r, 4).value
    Reg_Date = sheet.cell(r, 5).value

    # Assign values from each row
    values = (ID, name, Class, Section, Registered, Reg_Date)
    # Execute the SQL query
    cursor.execute(query, values)

# Close the cursor
cursor.close()
# Close the database
database.close()
# Print the results:
print("\n")
print("Fuckin'-A, I did it!")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print(f"I just imported {columns} columns, and {rows} rows to MySQL")








