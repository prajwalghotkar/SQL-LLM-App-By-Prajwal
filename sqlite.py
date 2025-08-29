import sqlite3

# Fix your database structure
conn = sqlite3.connect('STUDENT.db')
cursor = conn.cursor()

# Drop existing table if it has wrong structure
cursor.execute("DROP TABLE IF EXISTS STUDENT")

# Create table with correct structure
cursor.execute('''
    CREATE TABLE STUDENT (
        NAME TEXT,
        SURNAME TEXT,
        CLASS TEXT,
        SECTION TEXT
    )
''')

# Insert your data
student_data = [
    ('Prajwal', 'Ghotkar', 'Data Science', 'A'),
    ('Manaswi', 'Ghotkar', 'Devops', 'B'),
    ('Samikshya', 'Dhule', 'Devops', 'C'),
    ('Sejal', 'Dhule', 'Data Science', 'C'),
    ('Parth', 'Ghotkar', 'Cyber Security', 'B'),
    ('Kartik', 'Ghotkar', 'Devops', 'B'),
    ('Vivek', 'Ghotkar', 'MBBS-MD', 'A'),
    ('Pranjli', 'Ghotkar', 'MBBS', 'B'),
    ('Twinkal', 'Ghotkar', 'MBBS', 'B'),
    ('Janavi', 'Ghotkar', 'MBBS', 'B'),
    ('Utkarsh', 'Ghotkar', 'Pharmacy', 'B'),
    ('Nayana', 'Ghotkar', 'Devops', 'B'),
    ('Saurabh', 'Ghotkar', 'Cloud', 'B'),
    ('Devanshu', 'Dhule', 'Devops', 'B')
]

cursor.executemany('INSERT INTO STUDENT VALUES (?, ?, ?, ?)', student_data)
conn.commit()
conn.close()
print("Database fixed successfully!")