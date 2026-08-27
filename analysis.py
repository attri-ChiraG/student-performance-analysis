import pandas as pd

# Load the dataset
df = pd.read_csv("students.csv")

# Calculate average marks
df["Average"] = df[["Math", "Python", "English"]].mean(axis=1)

# Display the complete dataset
print("STUDENT PERFORMANCE ANALYSIS")
print("=" * 35)
print(df)

# Overall statistics
print("\nAverage Marks by Subject:")
print(df[["Math", "Python", "English"]].mean())

# Top 3 students
print("\nTop 3 Students:")
print(df.nlargest(3, "Average")[["Name", "Average"]])

# Attendance statistics
print("\nAverage Attendance:", df["Attendance"].mean())

# Highest performing student
top_student = df.loc[df["Average"].idxmax()]
print("\nHighest Performing Student:")
print(top_student[["Name", "Average", "Attendance"]])
