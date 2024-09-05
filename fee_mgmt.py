import json

#load from the json file
STUDENT_FILE = "student.json"

fee_struct = {
    2023: 50000,
    2024: 55000,
    2025: 60000
}

last_date_for_fees = {
    2023: "2023-12-31",
    2024: "2024-12-31",
    2025: "2025-12-31",
}

#load student from the file
def load_students():
        try:
            with open(STUDENT_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"{STUDENT_FILE} not found. Please ensure the file exists.")
            return {}

#save update data back to the json fike
def save_student(students):
    with open(STUDENT_FILE, 'w') as file:
        json.dump(students, file, indent=5)

#fee deposition function
def deposit_fee(students):
    id = int(input("Enter Student ID: "))
    if str(id) in students:
        st = students[str(id)]
        fee = fee_struct[st['year']]
        if st["percentage"] >= 95:
            print(f"{st['name']}, You have been awarded a scholarship")
            fee = 0
        st["fees_paid"] = True 
        save_student(students)
        print(f"Fee of {fee} has been deposited for {st['name']}")
    else:
        print("Student not found!")  

#check fee defaulter
def find_fee_defaulters_by_year(students): 
    year = int(input("Enter Year:"))
    default = []
    for st in students.values():
        if st["year"] == year and not st["fees_paid"]:
            default.append(st["name"])   
    if default:
        print(f"Fee default for the year, {year}: {','.join(default)}")
    else:
        print(f"No fee defaulters found for the year {year}")  

#unpaid fee students
def display_unpaid_students_by_year(students):
    year = int(input("Enter Year:")) 
    unpaid = []
    for st in students.values():
        if st["year"] == year and not st["fees_paid"]:
            unpaid.append(st["name"])
    if unpaid:
        print(f"Students who have not submitted fees for the year {year}: {','.join(unpaid)}")
    else:
        print(f"All students have submitted fees for the year {year}")  

#fee structure by year
def display_fee_structure_by_year():
    year = int(input("Enter Year:")) 
    if year in fee_struct:
        print(f"Fee structure for the year {year} is {fee_struct[year]}")
    else:
        print(f"No fee structure available for the year {year}") 

#last date of fee submission
def display_last_date_of_fee_submission():
    displayDate = int(input("Enter Year:"))
    if displayDate in last_date_for_fees:
        print(f"Last date of fee submission for the year {displayDate}: is {last_date_for_fees[displayDate]}")
    else:
        print(f"No last date available for the year {displayDate}") 

#report generate
def generate_report(students):
    with open("fee_report.txt", 'w') as file:
        file.write(f"==== DEFAULTER FEE REPORT ===== \n") 
        for year in fee_struct:
            defaulter = []
            for st in students.values():
                if st["year"] == year and not st["fees_paid"]:
                    defaulter.append(st["name"]) 
            file.write(f"YEAR: {year}\n")
            file.write(f"FEE: {fee_struct[year]}\n")
            file.write(f"LAST DATE: {last_date_for_fees[year]}\n")
            file.write(f"DEFAULTERS: {' '.join(defaulter) if defaulter else 'N/A'}\n\n")

    print("Report generated successfully!")                 

   

def main():

    students = load_students()
    if not students:
        return
    
    while True:
        print("\n === FEES MANAGEMENT SYSTEM ===")
        print("1. Deposit Fee")
        print("2. Find Fee Defaulters by Year")
        print("3. Display Students who have not Submitted Fees by Year")
        print("4. Display Fee Structure by Year")
        print("5. Display Last Date of Fee Submission by Year")
        print("6. Generate Report")
        choice = input("Enter your choice from (1-6): ")

        if choice == "1":
            deposit_fee(students)
        elif choice == "2":
            find_fee_defaulters_by_year(students)
        elif choice == "3":
            display_unpaid_students_by_year(students)
        elif choice == "4":
            display_fee_structure_by_year()
        elif choice == "5":
            display_last_date_of_fee_submission()
        elif choice == "6":
            generate_report(students)
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()                