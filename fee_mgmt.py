students = {
    1: {"name": "John", "year": 2023, "fees_paid": False, "percentage": 92},
    2: {"name": "Jane", "year": 2024, "fees_paid": False, "percentage": 97},
    3: {"name": "Sam", "year": 2023, "fees_paid": False, "percentage": 80},
    4: {"name": "Lisa ", "year": 2025, "fees_paid": False, "percentage": 88},
    5: {"name": "James", "year": 2023, "fees_paid": False, "percentage": 87},
    6: {"name": "Rose", "year": 2024, "fees_paid": False, "percentage": 96},
    7: {"name": "Marry", "year": 2025, "fees_paid": False, "percentage": 80},
    8: {"name": "Harry", "year": 2023, "fees_paid": False, "percentage": 95},
    9: {"name": "Ironman", "year": 2024, "fees_paid": False, "percentage": 79},
    10: {"name": "Potter", "year": 2025, "fees_paid": False, "percentage": 98},
    11: {"name": "Fan", "year": 2023, "fees_paid": False, "percentage": 99},
    12: {"name": "Table", "year": 2024, "fees_paid": False, "percentage": 65},
    13: {"name": "Chair", "year": 2025, "fees_paid": False, "percentage": 97},
    14: {"name": "Bed", "year": 2023, "fees_paid": False, "percentage": 81},
    15: {"name": "Cup", "year": 2024, "fees_paid": False, "percentage": 89},
    16: {"name": "Bag", "year": 2025, "fees_paid": False, "percentage": 33},
    17: {"name": "Cap", "year": 2023, "fees_paid": False, "percentage": 95},
    18: {"name": "Charger", "year": 2024, "fees_paid": False, "percentage": 75},
    19: {"name": "Drawer", "year": 2025, "fees_paid": False, "percentage": 89},
    20: {"name": "Door", "year": 2023, "fees_paid": False, "percentage": 96},
    21: {"name": "Handle", "year": 2024, "fees_paid": False, "percentage": 94},
    22: {"name": "Specs", "year": 2025, "fees_paid": False, "percentage": 98},
}

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

def deposit_fee():
    id = int(input("Enter Student ID: "))
    if id in students:
        st = students[id]
        fee = fee_struct[st['year']]
        if st["percentage"] >= 95:
            print(f"{st['name']}, You have been awarded a scholarship")
            fee = 0
        st["fees_paid"] = True 
        print(f"Fee of {fee} has been deposited for {st['name']}")
    else:
        print("Student not found!")  

def find_fee_defaulters_by_year(): 
    year = int(input("Enter Year:"))
    default = []
    for st in students.values():
        if st["year"] == year and not st["fees_paid"]:
            default.append(st["name"])   
    if default:
        print(f"Fee default for the year, {year}: {','.join(default)}")
    else:
        print(f"No fee defaulters found for the year {year}")  

def display_unpaid_students_by_year():
    year = int(input("Enter Year:")) 
    unpaid = []
    for st in students.values():
        if st["year"] == year and not st["fees_paid"]:
            unpaid.append(st["name"])
    if unpaid:
        print(f"Students who have not submitted fees for the year {year}: {','.join(unpaid)}")
    else:
        print(f"All students have submitted fees for the year {year}")  

def display_fee_structure_by_year():
    year = int(input("Enter Year:")) 
    if year in fee_struct:
        print(f"Fee structure for the year {year} is {fee_struct[year]}")
    else:
        print(f"No fee structure available for the year {year}") 

def display_last_date_of_fee_submission():
    displayDate = int(input("Enter Year:"))
    if displayDate in last_date_for_fees:
        print(f"Last date of fee submission for the year {displayDate}: is {last_date_for_fees[displayDate]}")
    else:
        print(f"No last date available for the year {displayDate}") 


def generate_report():
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
            file.write(f"DEFAULTER: {' '.join(defaulter) if defaulter else 'N/A'}\n\n")

    print("Report generated successfully!")                 

   

def main():
    
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
            deposit_fee()
        elif choice == "2":
            find_fee_defaulters_by_year()
        elif choice == "3":
            display_unpaid_students_by_year()
        elif choice == "4":
            display_fee_structure_by_year()
        elif choice == "5":
            display_last_date_of_fee_submission()
        elif choice == "6":
            generate_report()
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()                