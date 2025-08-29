from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai
import re

# Configure API Key
def configure_genai():
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        st.error("❌ GOOGLE_API_KEY not found! Create a .env file with your API key.")
        return False
    
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        st.error(f"❌ Error configuring API: {str(e)}")
        return False

# Simple SQL generator
def simple_sql_generator(question):
    question_lower = question.lower()
    
    # Pattern matching for simple queries
    if "how many" in question_lower or "count" in question_lower:
        return "SELECT COUNT(*) FROM STUDENT"
    elif "devops" in question_lower:
        return "SELECT * FROM STUDENT WHERE CLASS = 'Devops'"
    elif "data science" in question_lower:
        return "SELECT * FROM STUDENT WHERE CLASS = 'Data Science'"
    elif "cyber security" in question_lower:
        return "SELECT * FROM STUDENT WHERE CLASS = 'Cyber Security'"
    elif "mbbs" in question_lower:
        return "SELECT * FROM STUDENT WHERE CLASS LIKE '%MBBS%'"
    elif "cloud" in question_lower:
        return "SELECT * FROM STUDENT WHERE CLASS = 'Cloud'"
    elif "pharmacy" in question_lower:
        return "SELECT * FROM STUDENT WHERE CLASS = 'Pharmacy'"
    elif "ghotkar" in question_lower:
        return "SELECT * FROM STUDENT WHERE SURNAME = 'Ghotkar'"
    elif "dhule" in question_lower:
        return "SELECT * FROM STUDENT WHERE SURNAME = 'Dhule'"
    elif "section" in question_lower:
        if "section a" in question_lower:
            return "SELECT * FROM STUDENT WHERE SECTION = 'A'"
        elif "section b" in question_lower:
            return "SELECT * FROM STUDENT WHERE SECTION = 'B'"
        elif "section c" in question_lower:
            return "SELECT * FROM STUDENT WHERE SECTION = 'C'"
        else:
            return "SELECT * FROM STUDENT WHERE SECTION = 'B'"
    elif "prajwal" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Prajwal'"
    elif "manaswi" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Manaswi'"
    elif "samikshya" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Samikshya'"
    elif "sejal" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Sejal'"
    elif "parth" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Parth'"
    elif "kartik" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Kartik'"
    elif "vivek" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Vivek'"
    elif "pranjli" in question_lower or "pranjali" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Pranjli'"
    elif "twinkal" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Twinkal'"
    elif "janavi" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Janavi'"
    elif "utkarsh" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Utkarsh'"
    elif "nayana" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Nayana'"
    elif "saurabh" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Saurabh'"
    elif "devanshu" in question_lower:
        return "SELECT * FROM STUDENT WHERE NAME = 'Devanshu'"
    else:
        return "SELECT * FROM STUDENT"

# Function to retrieve query from database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        st.error(f"❌ Database error: {str(e)}")
        return None
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")
        return None

# Verify database exists and has correct structure
def verify_database():
    try:
        conn = sqlite3.connect('STUDENT.db')
        cursor = conn.cursor()
        
        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='STUDENT'")
        if not cursor.fetchone():
            conn.close()
            return False, "Database table does not exist"
        
        # Check if table has correct structure
        cursor.execute("PRAGMA table_info(STUDENT)")
        columns = [col[1] for col in cursor.fetchall()]
        if 'SURNAME' not in columns:
            conn.close()
            return False, "Database has incorrect structure"
        
        # Check if data exists
        cursor.execute("SELECT COUNT(*) FROM STUDENT")
        count = cursor.fetchone()[0]
        conn.close()
        
        if count == 0:
            return False, "Database is empty"
            
        return True, f"✅ Database verified: {count} records found"
            
    except Exception as e:
        return False, f"❌ Database connection failed: {str(e)}"

# Streamlit App
st.set_page_config(page_title="Student Database Query Tool", layout="wide")
st.title("🎓 Student Database Query Tool")

# Verify database instead of initializing
db_status, db_message = verify_database()

if db_status:
    st.sidebar.success(db_message)
else:
    st.sidebar.error(db_message)
    st.error("Please run 'sqlite.py' first to create the database!")
    st.stop()

# Don't use Gemini since it's not available
use_gemini = False
st.sidebar.warning("⚠️ Gemini not available. Using simple SQL generator")

# Sample questions
st.sidebar.header("💡 Sample Questions")
sample_questions = [
    "How many students are there?",
    "Show all students with surname Ghotkar",
    "List students with surname Dhule",
    "Show all students in Devops class",
    "How many students are in section B?",
    "Show students studying MBBS",
    "Find students in Data Science class",
    "Show students in Cyber Security",
    "List students in section A",
    "Find Vivek's details",
    "Show all students in Cloud class"
]

for i, question in enumerate(sample_questions):
    if st.sidebar.button(question, key=f"sample_{i}"):
        st.session_state.question = question

# Main interface
question = st.text_input(
    "Ask a question about students:",
    value=st.session_state.get('question', ''),
    placeholder="e.g., How many students have surname Ghotkar?"
)

if st.button("Generate Query", type="primary"):
    if not question:
        st.warning("Please enter a question first.")
    else:
        # Always use simple generator since Gemini is not available
        sql_query = simple_sql_generator(question)
        st.info("ℹ️ Using simple query generator")
        
        # Display and execute the query
        st.subheader("Generated SQL Query:")
        st.code(sql_query, language='sql')
        
        # Execute query
        results = read_sql_query(sql_query, "STUDENT.db")
        
        if results is not None:
            st.subheader("📊 Results:")
            if results and len(results) > 0:
                # Display results
                try:
                    # For COUNT queries
                    if "COUNT" in sql_query.upper():
                        st.success(f"Total students: {results[0][0]}")
                    else:
                        # For SELECT queries
                        display_data = {
                            "Name": [row[0] for row in results],
                            "Surname": [row[1] for row in results],
                            "Class": [row[2] for row in results],
                            "Section": [row[3] for row in results]
                        }
                        st.table(display_data)
                        st.success(f"✅ Found {len(results)} records")
                except Exception as e:
                    st.error(f"Error displaying results: {e}")
            else:
                st.info("ℹ️ No results found for this query")
        else:
            st.error("❌ Failed to execute query")

# Display database contents
if st.sidebar.checkbox("Show all students in database"):
    all_students = read_sql_query("SELECT * FROM STUDENT", "STUDENT.db")
    if all_students:
        st.sidebar.subheader("All Students (14 total)")
        for student in all_students:
            st.sidebar.write(f"{student[0]} {student[1]} - {student[2]} ({student[3]})")