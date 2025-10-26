
import csv

# ---------- Function to read CSV file ----------
def read_employee_data(filename):
    employees = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    employees.append({
                        "Name": row["Name"].strip(),
                        "Department": row["Department"].strip(),
                        "Score": float(row["Score"].replace(",", "")),  # remove commas if any
                        "Bonus": row["Bonus Grade"].strip()
                    })
                except ValueError:
                    print(f"⚠️ Skipping invalid record: {row}")
        return employees
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return []


# ---------- Display the report ----------
def generate_report(employees):
    print("===== Employee Performance & Bonus Management System =====\n")
    print(f"{'Name':<10} | {'Department':<12} | {'Score':<15} | {'Bonus Grade'}")
    print("-" * 60)

    for emp in employees:
        print(f"{emp['Name']:<10} | {emp['Department']:<12} | {emp['Score']:<15,.1f} | {emp['Bonus']}")

    top = employees[0]
    print(f"\n🏆 Top Performer: {top['Name']} — Score {top['Score']:,} (Bonus Grade: {top['Bonus']})")


# ---------- Main Program ----------
def main():
    filename = "employee_data.csv"
    employees = read_employee_data(filename)

    if not employees:
        print("⚠️ No employee data found. Please check your CSV file.")
        return

    # Sort employees by score (descending)
    employees.sort(key=lambda x: x["Score"], reverse=True)

    # Display report
    generate_report(employees)


# ---------- Run the program ----------
if __name__ == "__main__":
    main()