# Q:o Create a dictionary with 3 students' names as keys and their scores as values. 
# Print the score of a specific student by their name.
# Create a dictionary with students' names and their scores
students_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Print the score of a specific student by their name
student_name = "Bob"
if student_name in students_scores:
    print(f"{student_name}'s score is: {students_scores[student_name]}")
else:
    print(f"Student {student_name} not found in the dictionary.")
