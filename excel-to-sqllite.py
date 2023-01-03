import sqlite3
import pandas as pd
import openpyxl

con = sqlite3.connect('C:\\Users\\Troy\\sales.db')
wb = pd.read_excel('test.xlsx', sheet_name=None)

for sheet in wb:
    wb[sheet].to_sql(sheet, con, index=False)
con.commit()
con.close()