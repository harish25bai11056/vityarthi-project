# Research Paper Archival and Tracking System (R-PATS)

* ## Overview
R-PATS is a modular desktop application built with Python and SQLite. It streamlines the management of student research papers by providing a centralized interface for submission, status tracking, and compliance reporting. It replaces error-prone manual methods with a structured, persistent database solution.

* ## Features
1. Student & Submission Management: Create and update student records with validation logic.
2. Status Tracking: Manage paper status (Submitted, Under Review, Approved, Rejected) with timestamp logging.
3. Compliance Reporting: Generate summaries of approval rates and filter papers by status.

* ## Technologies Used
1. Language: Python 3.x
2. Database: SQLite 3
3. Concepts: Object-Oriented Programming (OOP), Modular Architecture.

* ## Steps to Install & Run

### 1.Clone the repository:
git clone <repository-url>
cd R-PATS
### 2.Run the main application:
python main.py
(The database file student_research.db will be created automatically).

* Instructions for Testing
1. Submit Paper: Select Option 1. Enter Reg No V001, Name John Doe, Dept CSE, Title AI in Healthcare.
2. Update Status: Select Option 2. Enter V001 and status Approved.
3. Verify Error Handling: Select Option 3 (View). Enter V999 (non-existent). Listen for the system beep (\a) and error message.
4. Check Report: Select Option 4 to see the Approval Rate calculation.
