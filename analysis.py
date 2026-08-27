import pandas as pd

# Load the dataset
df = pd.read_csv("students.csv")

print("ORIGINAL DATASET")
print(df)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_yduplicates()

# Calculate average marks
subjects = ["Math", "Python", "English"]
df["Average"] = df[subjects].mean(axis=1)

# Overall statistics
print("\nAverage Marks by Subject:")
print(df[subjects].mean().round(2))

# Top 3 students
print("\nTop 3 Students:")
print(
    df.nlargest(3, "Average")[["Name", "Average"]]
    .round(2)
)

# Average attendance
print("\nAverage Attendance:")
print(round(df["Attendance"].mean(), 2))

# Correlation
correlation = df["Attendance"].corr(df["Average"])

print("\nAttendance vs Average Marks Correlation:")
print(round(correlation, 2))

# Highest performing student
top_student = df.loc[df["Average"].idxmax()]

print("\nHighest Performing Student:")
print(
    top_student[["Name", "Average", "Attendance"]]
)
