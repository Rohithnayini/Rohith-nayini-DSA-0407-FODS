
import numpy as np

# 4x4 matrix: Math, Science, English, History
student_scores = np.array([
    [85, 90, 78, 88],
    [92, 85, 80, 75],
    [78, 95, 85, 80],
    [88, 90, 92, 85]
])

# Calculate average for each subject
averages = np.mean(student_scores, axis=0)

subjects = ["Math", "Science", "English", "History"]

# Display subject averages
for i in range(len(subjects)):
    print(subjects[i], "Average:", averages[i])

# Find subject with highest average
highest_index = np.argmax(averages)

print("Highest average subject:", subjects[highest_index])
print("Highest average score:", averages[highest_index])
