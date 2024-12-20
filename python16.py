#Combine lists, tuples, and dictionaries in one program: 
# Create a dictionary where each key is a student's name, and the value is a tuple containing 
#their scores in three subjects. 
# Write functions to: 
#1. Calculate and print the average score of each student. 
#2. Find the student with the highest average score. 
# Step 1: Create a dictionary with students' names and their scores in three subjects
students_scores = {
    "Alice": (85, 90, 88),
    "Bob": (78, 82, 80),
    "Charlie": (92, 95, 94)
}

# Function to calculate and print the average score of each student
def calculate_average_scores(students_scores):
    for student, scores in students_scores.items():
        average_score = sum(scores) / len(scores)
        print(f"{student}'s average score is: {average_score:.2f}")

# Function to find the student with the highest average score
def find_top_student(students_scores):
    top_student = None
    highest_average = 0
    for student, scores in students_scores.items():
        average_score = sum(scores) / len(scores)
        if average_score > highest_average:
            highest_average = average_score
            top_student = student
    return top_student, highest_average

# Calculate and print the average score of each student
calculate_average_scores(students_scores)

# Find and print the student with the highest average score
top_student, highest_average = find_top_student(students_scores)
print(f"The student with the highest average score is {top_student} with an average score of {highest_average:.2f}")
