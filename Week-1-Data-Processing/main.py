import csv
import numpy as np


# Load student data from the CSV file
def load_data(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


# Remove extra spaces from student names
def clean_name(name):
    return name.strip()


# Check whether a mark is valid
def clean_mark(mark):
    try:
        mark = float(mark)

        if 0 <= mark <= 100:
            return mark

        return None

    except ValueError:
        return None


# Clean the student records
def clean_data(data):
    cleaned_data = []
    removed_records = 0

    for row in data:
        name = clean_name(row["name"])
        mark = clean_mark(row["mark"])

        if name != "" and mark is not None:
            cleaned_data.append({"name": name, "mark": mark})
        else:
            removed_records += 1

    return cleaned_data, removed_records


# Calculate student results using NumPy
def process_data(data):
    if not data:
        print("No valid student records to process.")
        return

    marks = np.array([student["mark"] for student in data])

    average = np.mean(marks)
    highest = np.max(marks)
    lowest = np.min(marks)
    passed = np.sum(marks >= 50)

    print("\n========== STUDENT MARKS REPORT ==========")
    print("Valid students:", len(data))
    print("Average mark:", round(average, 2))
    print("Highest mark:", highest)
    print("Lowest mark:", lowest)
    print("Students passed:", int(passed))
    print("Students failed:", len(data) - int(passed))
    print("==========================================")


# Main function
def main():
    raw_data = load_data("students.csv")

    cleaned_data, removed_records = clean_data(raw_data)

    print("Original records:", len(raw_data))
    print("Removed records:", removed_records)

    process_data(cleaned_data)


# Start the program
if __name__ == "__main__":
    main()