# Project Statement: Research Paper Archival and Tracking System (R-PATS)

* ## Problem Statement
Academic departments currently rely on fragmented systems—such as spreadsheets, email threads, and physical logbooks—to track student research paper submissions.
This manual approach leads to data redundancy, difficulty in tracking the real-time review status of papers 
(e.g., "Under Review" vs "Approved"), and inefficiencies in generating compliance reports for graduation audits. There is a need for a centralized, automated system to digitize this workflow.

* ## Scope of the Project
The project focuses on the administrative management of student research metadata. It covers the lifecycle of a paper from initial submission to final approval.
1. In Scope: Student registration, Paper metadata storage, Workflow status updates, Compliance reporting, Data persistence.
2. Out of Scope: Storage of physical PDF files (file handling), Cloud hosting, User authentication.

* ## Target Users
1. Department Administrator: To manage student records and generate reports.
2. Faculty Reviewer: To update the status of papers based on review outcomes.
3. Compliance Officer: To view statistics on how many students have successfully published.

* ## High-Level Features
1. Data Persistence: Uses SQLite to store records permanently.
2. Workflow Management: Validates status transitions (e.g., Submitted -> Under Review -> Approved).
3. Search & Retrieval: Instant lookup of records via Registration Number.
4. Analytics: Automated calculation of department-wide approval rates.  
