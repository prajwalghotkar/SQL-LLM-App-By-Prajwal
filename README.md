# 📊 SQL LLM App — Natural Language to SQL Query Generator
## 🔍 Convert English Questions to SQL using Google Gemini + Streamlit + SQLite

# 🚀 Overview
### SQL LLM App is an intelligent Streamlit web app that translates natural language questions into SQL queries using Google Gemini Pro and fetches data from a local SQLite database.

### Just type questions like:

#### -->“Show all students whose surname is Ghotkar”
#### -->“How many students are in MBBS?”

#### …and the app will respond with the correct SQL output — instantly.

#### Here are a few examples:

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


# 🧠 Project Description
### This project is a Natural Language to SQL Query App powered by Google Gemini Pro, built using Python, Streamlit, and SQLite. It allows users to ask database-related questions in plain English — and get actual SQL query results in response.This project allows users to enter questions in plain English (like "Show all students in Data Science class?"), and it automatically converts them into SQL queries and runs them on a local STUDENT database using SQLite.

### The backend logic uses a Large Language Model (LLM) to translate user questions into SQL queries, which are then executed on a local STUDENT.db SQLite database. The database stores records of students, including fields like Name, Last Name, Class, and Section.

#### 🔍 Example Use-Cases:
##### Ask: “How many students are in Devops class?” → Get exact count.

##### Ask: “Show all students with last name Ghotkar” → Get matching rows.

##### Ask: “List students from section B” → Fetch filtered data.

#### 🎯 Key Features:

##### * Convert natural English queries to SQL in real-time
##### * Display data using Streamlit
##### * Powered by Gemini Pro from Google Generative AI
##### * Local lightweight SQLite database for fast response

# 🧠 Tech Stack

### * LLM: Google Gemini Pro (gemini-pro)
### * Frontend: Streamlit
### * Database: SQLite
### * Environment: Python 3.10 + dotenv for secure API key loading

# 🗃️ Database Schema

### Table Name: STUDENT

Column Name	     Description

NAME ----------->	First Name

LAST_NAME	-----------> Last Name / Surname

CLASS	Course ----------->	SECTION	Section (A/B/C)

# 📦 Project Files

### SQL_LLM_APP/
#### ├──> sqlite.py         # Script to create STUDENT.db and insert data
#### ├──> sql.py            # Streamlit app to handle user input and query
#### ├──> requirements.txt  # All required Python libraries
#### ├──> .env              # Contains GOOGLE_API_KEY (not shared publicly)
#### └──> STUDENT.db        # Auto-generated SQLite database

# 📥 Setup Instructions (Windows + Anaconda)
#### Follow these terminal commands to run the project:

#### Step 1: Navigate to project folder
##### cd OneDrive\Desktop\SQL_LLM_APP
<img width="1920" height="997" alt="Screenshot 2025-07-10 190133" src="https://github.com/user-attachments/assets/cb7280e1-c613-4955-a97e-9bedef8ca9f6" />


#### Step 2: Create a virtual environment with Python 3.10
##### conda create -p venv python=3.10 -y
<img width="1920" height="997" alt="Screenshot 2025-07-10 190133" src="https://github.com/user-attachments/assets/a8af7e4f-e377-4ae2-8ede-ee18a94bd0c7" />

#### Step 3: Activate the environment
##### conda activate ./venv
<img width="1920" height="266" alt="Screenshot 2025-07-10 194726" src="https://github.com/user-attachments/assets/b0c10edb-fc25-4b93-8df8-83cd5c05a407" />

#### Step 4: Install dependencies
##### pip install -r requirements.txt
<img width="1920" height="992" alt="Screenshot 2025-07-10 190202" src="https://github.com/user-attachments/assets/bdc4a0ba-c89a-4e91-b864-f17796000f75" />

#### Step 5: Insert sample student data into SQLite DB
##### python sqlite.py
<img width="1920" height="1009" alt="Screenshot 2025-07-10 190216" src="https://github.com/user-attachments/assets/73cec51e-2e86-41c8-bf94-df91b94598ce" />


#### Step 6: Launch the Streamlit app
##### streamlit run sql.py
<img width="1920" height="1013" alt="Screenshot 2025-07-10 190225" src="https://github.com/user-attachments/assets/76f8742c-92e1-4039-8989-c334f5a1a883" />

✅ App will open in browser: http://localhost:8501

<img width="1920" height="957" alt="Screenshot 2025-07-10 190505" src="https://github.com/user-attachments/assets/09ad5d6f-dae4-4b1b-b32d-fe7c0c09df2b" />

# 💬 Sample Questions You Can Try
####        English Input	                    SQL Query
##### How many students are there? ----->	SELECT COUNT(*) FROM STUDENT;
##### Show all students in Devops  ----->	SELECT * FROM STUDENT WHERE CLASS = 'Devops';
##### List students in section B	 -----> SELECT * FROM STUDENT WHERE SECTION = 'B';
##### Who has surname Ghotkar?	   -----> SELECT * FROM STUDENT WHERE LAST_NAME = 'Ghotkar';

# 🔮 Future Scope
#### This project demonstrates how natural language processing and LLMs (like Gemini) can be used to simplify database interactions. Below are some possible future enhancements:

#### 🔍 Support for Complex Queries
###### Add support for advanced SQL operations such as JOIN, GROUP BY, ORDER BY, and nested queries to handle more complex business questions.

##### 📈 Data Visualization
###### Integrate libraries like matplotlib, seaborn, or Plotly to show visual insights (charts, graphs) directly from the query results.

##### 📂 Upload Custom Databases
###### Allow users to upload their own .db or .csv files and dynamically generate prompts based on those schemas.

##### 🧠 Fine-Tuned Prompt Engineering
###### Continuously improve prompt templates using few-shot learning and feedback loops to make query generation more accurate.

##### 👥 User Authentication
###### Add login functionality for saving user sessions and personal query history.

##### 🛡️ Query Validation & Security
###### Include validation to prevent malformed or harmful SQL statements, especially in production deployments.

##### 🌐 Deployment on Cloud
###### Deploy the application using platforms like Streamlit Cloud, Hugging Face Spaces, or on your own via AWS, GCP, or Heroku.

##### 📜 Query Logs & Audit Trails
###### Maintain a log of all natural language inputs and the corresponding SQL queries for analysis, debugging, or training future models.

##### 🗣️ Voice Input Integration
###### Integrate voice-to-text input using tools like Google Speech API to allow hands-free interaction.

##### 📦 API Integration
###### Wrap the functionality as a REST API so that other applications can interact with it programmatically.



🧑‍💻
Prajwal Ghotkar
https://github.com/prajwalghotkar
