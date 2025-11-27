# Project Title: Research Paper Archival and Tracking System (R-PATS)

## Overview of the project
R-PATS is a desktop-based application developed to help academic departments manage and track student research paper submissions. Currently, many departments use manual methods like spreadsheets which are prone to errors and data loss. This project solves that problem by providing a centralized system where students can register their details and submit up to three research papers. The system saves all data permanently in a database and allows users to search for student records using their Registration Number.

## Features
* Student Registration: Allows entry of Student Name, Registration Number (Mandatory),and College Name.
* Paper Archival: Supports the submission of up to 3 separate research papers per student.
* Search Functionality: Users can instantly search and retrieve a student's submission history using their unique Registration Number.
* Data Persistence: Uses a local SQLite database (college_project.db) so data is saved even after the program closes.
* Security: Implements basic hashing to secure student data.
* Activity Logging: Automatically records system activities (like new registrations) into a text file (activity_log.txt).

## Technologies/tools used
* Programming Language: Python 3
* Database: SQLite (Built-in)
* Development Environment: VS Code / IDLE / Terminal
* Key Python Libraries:
* sqlite3 (Database management)
* os (System operations)
* hashlib (Data security)
* datetime (Timestamping)

## Steps to install & run the project
1. Prerequisites:
* Ensure you have Python installed on your computer. You can check this by typing python --version in your terminal.
2. Installation:
* Download the main.py file to a folder on your computer.
* No external libraries need to be installed (pip install is not required) as the project uses standard Python libraries.
3. Running the Application:
* Open your Command Prompt (Windows) or Terminal (Mac/Linux).
* Navigate to the folder where you saved the file.
4. Run the following command:
* Bash
* python main.py

## Instructions for testing
To verify the project is working correctly, follow these test scenarios:
1. Test: Register a Student
* Run the program.
* Choose Option 1 (Registration).
* Enter Name: Harish Kumar
* Try pressing Enter without typing a Registration No (System should ask again).
* Enter Registration No: 25BAI11056
* Enter College: VIT BHOPAL
* Enter Paper 1: Machine Learning Basics.
* Enter Paper 2: Cloud Security.
* Leave Paper 3 empty and press Enter.
* Expected Result: The system prints "Success!" and saves the data.
2. Test: Search for a Student
* Choose Option 2 (Search).
* Enter Registration No: 25BAI11056
* Expected Result: The system displays Harish Kumar's details and the two papers he submitted.
3. Test: Exit
* Choose Option 3.
* Expected Result: The application closes safely.

## Screanshots
Its been provided in Project PDF
