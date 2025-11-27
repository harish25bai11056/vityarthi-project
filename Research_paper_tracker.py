import sqlite3
import os
import hashlib
from datetime import datetime

# Database file name
db_name = "college_project.db"

# --- 1. DATABASE MANAGEMENT ---
class DBHandler:
    def __init__(self):
        self.init_db()

    def get_conn(self):
        return sqlite3.connect(db_name)

    def init_db(self):
        conn = self.get_conn()
        cursor = conn.cursor()
        
        # Table for Student Details
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                reg_no TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                college_name TEXT,
                security_hash TEXT
            )
        """)
        
        # Table for Research Papers
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS papers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                reg_no TEXT,
                date_added TEXT,
                FOREIGN KEY(reg_no) REFERENCES students(reg_no)
            )
        """)
        conn.commit()
        conn.close()

    def add_student(self, reg, name, college, hash_code):
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            # Insert or Update if exists
            cursor.execute("INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?)", (reg, name, college, hash_code))
            conn.commit()
            conn.close()
        except:
            pass

    def add_paper(self, title, reg):
        conn = self.get_conn()
        cursor = conn.cursor()
        date = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO papers (title, reg_no, date_added) VALUES (?, ?, ?)", (title, reg, date))
        conn.commit()
        conn.close()

    def get_student_data(self, reg):
        conn = self.get_conn()
        cursor = conn.cursor()
        query = """
            SELECT s.name, s.college_name, p.title, p.date_added 
            FROM students s 
            LEFT JOIN papers p ON s.reg_no = p.reg_no 
            WHERE s.reg_no = ?
        """
        cursor.execute(query, (reg,))
        rows = cursor.fetchall()
        conn.close()
        return rows

# --- 2. LOGIC & UTILITIES ---
class SystemLogic:
    def __init__(self):
        self.db = DBHandler()

    def write_log(self, text):
        # Basic file logging
        try:
            f = open("activity_log.txt", "a")
            f.write(f"{datetime.now()}: {text}\n")
            f.close()
        except:
            pass

    def secure_data(self, txt):
        # Simple hash for security requirement
        return hashlib.sha256(txt.encode()).hexdigest()

    def register_entry(self, name, reg, college, p1, p2, p3):
        # Create hash
        h = self.secure_data(reg + name)
        
        # Save student
        self.db.add_student(reg, name, college, h)
        
        # Save papers individually
        count = 0
        if p1 != "":
            self.db.add_paper(p1, reg)
            count += 1
        if p2 != "":
            self.db.add_paper(p2, reg)
            count += 1
        if p3 != "":
            self.db.add_paper(p3, reg)
            count += 1
            
        self.write_log(f"Registered {reg} with {count} papers")
        return count

    def find_data(self, reg):
        return self.db.get_student_data(reg)

# --- 3. USER INTERFACE ---
class AppInterface:
    def __init__(self):
        self.logic = SystemLogic()

    def main_menu(self):
        while True:
            # Clear screen command
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

            print("---------------------------------")
            print(" RESEARCH PAPER TRACKING SYSTEM")
            print("---------------------------------")
            print("1. Registration & Paper Submission")
            print("2. Search Paper by Registration No")
            print("3. Exit")
            print("---------------------------------")
            
            choice = input("Enter Choice (1-3): ")

            if choice == '1':
                print("\n[ NEW ENTRY ]")
                nm = input("Enter Name: ")
                
                # Loop to ensure Reg No is entered
                rg = ""
                while rg == "":
                    rg = input("Enter Registration No (Mandatory): ")
                
                clg = input("Enter College Name: ")
                
                print("\n[ ENTER PAPERS (Max 3) ]")
                paper1 = input("1. Name of Research Paper: ")
                paper2 = input("2. Name of Research Paper: ")
                paper3 = input("3. Name of Research Paper: ")
                
                c = self.logic.register_entry(nm, rg, clg, paper1, paper2, paper3)
                print(f"\nSuccess! Saved {c} papers.")
                input("Press Enter to continue...")

            elif choice == '2':
                print("\n[ SEARCH ]")
                find_reg = input("Enter Registration No: ")
                data = self.logic.find_data(find_reg)
                
                if len(data) == 0:
                    print("No records found.")
                else:
                    print("\nStudent:", data[0][0])
                    print("College:", data[0][1])
                    print("Papers:")
                    found = False
                    for row in data:
                        if row[2]:
                            print(f"- {row[2]} ({row[3]})")
                            found = True
                    if not found:
                        print("No papers submitted.")
                
                input("\nPress Enter to continue...")

            elif choice == '3':
                print("Exiting...")
                break

if __name__ == "__main__":
    app = AppInterface()
    app.main_menu()
