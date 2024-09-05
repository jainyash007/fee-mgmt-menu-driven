Fee Management System


This Python-based Fee Management System allows managing student fee records, identifying defaulters, generating reports, and more. It is a simple, menu-driven program that processes fee information based on the student's academic year.

Features
1. Deposit Fee: Allows depositing student fees and checks for a scholarship if the student's score is 95% or higher.
2. Find Fee Defaulters by Year: Displays students who have not paid fees for a specific year.
3. Display Students Who Have Not Submitted Fees by Year: Lists students who haven’t submitted fees based on the year.
4. Display Fee Structure by Year: Shows the fee structure for the selected academic year.
5. Display Last Date of Fee Submission by Year: Displays the last fee submission date for each academic year.
6. Generate Report: Generates a report that includes fee defaulters, fee structures, and last dates for all years, and saves it to a text file.


How It Works - 
The program operates on a simple menu-driven interface, where users can choose from multiple options to interact with the fee management system.
1. Deposit Fee: The user enters the student's ID, and the system checks their score. If their score is 95% or more, they are awarded a scholarship (no fee). The student is then marked as having paid the fee.
2. Find Fee Defaulters: The user inputs the year, and the system lists students from that year who haven't paid their fees.
3. Display Unpaid Students: The user inputs a year, and the system lists students from that year who have not yet paid.
4. Display Fee Structure: The user inputs a year, and the system displays the fee amount for that year.
5. Display Last Date of Fee Submission: The user inputs a year, and the system shows the last date to submit fees for that academic year.
6. Generate Report: The system generates a report of defaulters and fee structures and saves it to a fee_report.txt file.


How to Use - 
Clone the Repository or Download the File
git clone https://github.com/your-username/fee-mgmt-system.git

Run the Program
Open your terminal and navigate to the directory where the program is located, then run:
python fee_mgmt.py


The program will present you with a menu to choose an action:
Fee Management System
1. Deposit Fee
2. Find Fee Defaulters by Year
3. Display Students who have not Submitted Fees by Year
4. Display Fee Structure by Year
5. Display Last Date of Fee Submission by Year
6. Generate Report
   
Interact with the Program
Option 1: Input the student ID to deposit the fee.
Option 2: Input the year to list fee defaulters.
Option 3: Input the year to display unpaid students.
Option 4: Input the year to display the fee structure.
Option 5: Input the year to display the last date of fee submission.
Option 6: The program will generate a fee_report.txt file with all the details.

Sample Output
Generated Report File (fee_report.txt)
Year: 2023
Fee: $5000
Last Date: 2023-12-31
Defaulters: John Doe, Sam Brown

Year: 2024
Fee: $5500
Last Date: 2024-12-31
Defaulters: None

Year: 2025
Fee: $6000
Last Date: 2025-12-31
Defaulters: None

<img width="1552" alt="Screenshot 2024-09-05 at 12 37 59 PM" src="https://github.com/user-attachments/assets/15f07dc9-269e-4068-9fad-076b12d15af5">
<img width="1440" alt="Screenshot 2024-09-05 at 12 32 59 PM" src="https://github.com/user-attachments/assets/bcec6117-473a-4e51-b30b-3b2219e9be09">
