import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\sayom\OneDrive\Documents\Database01.accdb;') #LOCATION OF FILE \Users\sayom\OneDrive\Documents\Database01
    print("Database is Connected")


except pyodbc.Error:
    print("Error in Connection")

