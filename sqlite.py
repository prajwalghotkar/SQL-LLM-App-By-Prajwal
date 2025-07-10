# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('STUDENT.db')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Creating table
table = """CREATE TABLE STUDENT(NAME VARCHAR(255),LAST_NAME VARCHAR(255),CLASS VARCHAR(255),
SECTION VARCHAR(255));"""
cursor.execute(table)

# Queries to INSERT records. 
cursor.execute('''INSERT INTO STUDENT VALUES ('Prajwal', 'Ghotkar', 'Data Science', 'A')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Manaswi', 'Ghotkar', 'Devops', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Samikshya', 'Dhule', 'Devops', 'C')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sejal', 'Dhule', 'Data Science', 'C')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Parth', 'Ghotkar', 'Cyber Security', 'B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Kartik', 'Ghotkar', 'Devops', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vivek', 'Ghotkar', 'MBBS-MD', 'A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Pranjli', 'Ghotkar', 'MBBS', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Twinkal', 'Ghotkar', 'MBBS', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Janavi', 'Ghotkar', 'MBBS', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Utkarsh', 'Ghotkar', 'Pharmacy', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Nayana', 'Ghotkar', 'Devops', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Saurabh', 'Ghotkar', 'Cloud', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Devanshu', 'Dhule', 'Devops', 'B')''')    

# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()