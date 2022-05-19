import pyodbc




try:

    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\admin\Desktop\Database01.accdb;')
    print("Database is Connected")


    database = connect.cursor()
    database.execute('''
                    INSERT INTO Table1 (ID, FullName, Age, Birthdate, SemGrade, Address)
                    VALUES(?,?,?,?,?,?) ''',
                    (11,'Jan Rovick M. Causaren', 19,'1/16/2003',  90, 'Cavite'))



    database.commit()

    print("Data Added")

except pyodbc.Error:
    print("Error in Connection")