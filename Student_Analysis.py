import pandas as pd
import matplotlib.pyplot as plt

# Loads Excel data
file_path = 'students.xlsx'  # Change if your file name is different
df = pd.read_excel(file_path)

# Calculates student average(BR)
df['Average'] = df.iloc[:, 1:].mean(axis=1)

# Calculates subject-wise average(LR)
subject_averages = df.iloc[:, 1:-1].mean()

# BAR Chart for Individual Student Performance
for index, row in df.iterrows():
    student_name = row['Name']
    subjects = df.columns[1:-1]
    scores = row[1:-1]

    plt.figure(figsize=(8, 5))
    plt.bar(subjects, scores, color='skyblue')
    plt.title(f"{student_name}'s Marks")
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.ylim(0, 100)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"{student_name}_marks_bar_chart.png")
    plt.close()

# LINE Chart for Subject-wise Average Trend
plt.figure(figsize=(8, 5))
plt.plot(subject_averages.index, subject_averages.values, marker='o', color='green')
plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("subject_average_trend_line_chart.png")
plt.show()

# Prints dataframe summary
print("\nStudent Performance Summary:")
print(df[['Name', 'Average']])
