import pandas as pd

# Create employee details
employees = {
    "Name": ["Kiran", "Ravi", "Suresh", "Priya", "Anu"],
    "Age": [23, 25, 22, 24, 21],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [30000, 45000, 25000, 50000, 35000]
}

# Convert the data into a DataFrame
df = pd.DataFrame(employees)

print("Employee Details:")
print(df)

# Sort employees by salary from lowest to highest
print("\nEmployees Sorted by Salary (Ascending):")
print(df.sort_values(by="Salary"))

# Sort employees by salary from highest to lowest
print("\nEmployees Sorted by Salary (Descending):")
print(df.sort_values(by="Salary", ascending=False))

# Sort employees by department and salary
print("\nEmployees Sorted by Department and Salary:")
print(df.sort_values(by=["Department", "Salary"]))

# Sort employees by age from oldest to youngest
print("\nEmployees Sorted by Age (Descending):")
print(df.sort_values(by="Age", ascending=False))
