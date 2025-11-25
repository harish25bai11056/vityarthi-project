import sqlite3
import json
import time

# --- Database Setup Section ---
def initialize_database():
    """
    Creates the database and table if they don't exist.
    We use JSON to store the list of papers within a single database column.
    """
    conn = sqlite3.connect('university_research.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_research (
            reg_number TEXT PRIMARY KEY,
            student_name TEXT,
            college_name TEXT,
            department TEXT,
            papers TEXT
        )
    ''')
    conn.commit()
    conn.close()

# --- Data Entry Section ---
def add_student_record():
    print("\n--- ADD NEW STUDENT RESEARCH RECORD ---")
    
    # 1. College and Department Inputs
    college = input("Enter College Name: ").strip()
    dept = input("Enter Department Name: ").strip()
    
    # 2. Separate Inputs for Name and Reg No (As requested)
    name = input("Enter Student Name: ").strip()
    reg_no = input("Enter Registration Number (Unique ID): ").strip()
    
    # Check if Reg No is empty
    if not reg_no:
        print("Error: Registration Number is mandatory.")
        return

    # 3. Research Paper Inputs (Limited to 3)
    papers = []
    print("\n--- Enter Research Papers (Max 3) ---")
    print("Press 'Enter' without typing to skip remaining slots.")
    
    for i in range(1, 4): # Loops 1, 2, 3
        paper_title = input(f"Paper {i} Title: ").strip()
        
        # If user leaves input blank, stop asking
        if paper_title == "":
            break
            
        papers.append(paper_title)
    
    if len(papers) == 0:
        papers.append("No papers submitted")

    # Serialize list to JSON string for storage
    papers_json = json.dumps(papers)

    # 4. Save to Database
    try:
        conn = sqlite3.connect('university_research.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO student_research (reg_number, student_name, college_name, department, papers)
            VALUES (?, ?, ?, ?, ?)
        ''', (reg_no, name, college, dept, papers_json))
        
        conn.commit()
        conn.close()
        print(f"\n[SUCCESS] Record saved for {name} ({reg_no}).")
        
    except sqlite3.IntegrityError:
        print(f"\n[ERROR] A student with Registration Number '{reg_no}' already exists.")

# --- Search Section ---
def find_paper_by_reg_no():
    print("\n--- SEARCH RESEARCH PAPERS ---")
    
    # 1. Input Registration Number to search
    search_reg = input("Enter Registration Number to search: ").strip()
    
    conn = sqlite3.connect('university_research.db')
    cursor = conn.cursor()
    
    # 2. Query the database
    cursor.execute("SELECT * FROM student_research WHERE reg_number=?", (search_reg,))
    result = cursor.fetchone()
    conn.close()
    
    # 3. Display Results
    if result:
        # result tuple structure: (reg_no, name, college, dept, papers_json)
        reg_no = result[0]
        name = result[1]
        college = result[2]
        dept = result[3]
        papers_list = json.loads(result[4]) # Convert string back to Python List
        
        print("\n" + "="*30)
        print(f"Student:    {name}")
        print(f"Reg No:     {reg_no}")
        print(f"College:    {college}")
        print(f"Department: {dept}")
        print("-" * 30)
        print("Research Papers Authored:")
        for idx, paper in enumerate(papers_list, 1):
            print(f"  {idx}. {paper}")
        print("="*30)
    else:
        print(f"\n[NOT FOUND] No records found for Registration Number: {search_reg}")

# --- Main Menu System ---
def main():
    initialize_database()
    
    while True:
        print("\n" + "*"*40)
        print(" UNIVERSITY RESEARCH ARCHIVE SYSTEM")
        print("*"*40)
        print("1. Add Student & Research Data")
        print("2. Find Papers by Registration No")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            add_student_record()
        elif choice == '2':
            find_paper_by_reg_no()
        elif choice == '3':
            print("Exiting System. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")
        
        time.sleep(1) # Small pause for better user experience

if __name__ == "__main__":
    main()
