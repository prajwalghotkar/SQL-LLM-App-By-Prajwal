from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
     """
    You are an expert in converting English questions into SQL queries!
    The SQL database is named STUDENT and has the following columns - 
    NAME, SURNAME, CLASS, SECTION

    Here are a few examples:

    Example 1 - How many student records are there? 
    The SQL command will be: SELECT COUNT(*) FROM STUDENT;

    Example 2 - Show all students in the Devops class.
    The SQL command will be: SELECT * FROM STUDENT WHERE CLASS = 'Devops';

    Example 3 - List all students in section B.
    The SQL command will be: SELECT * FROM STUDENT WHERE SECTION = 'B';

    Example 4 - Get all students whose surname is Ghotkar.
    The SQL command will be: SELECT * FROM STUDENT WHERE SURNAME = 'Ghotkar';

    Example 5 - How many students are studying MBBS?
    The SQL command will be: SELECT COUNT(*) FROM STUDENT WHERE CLASS = 'MBBS';

    Important Notes:
    - Only return the SQL query as output.
    - Do NOT include ``` or any code block formatting.
    - Do NOT mention the word "SQL" in your answer.
    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"STUDENT.db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)








