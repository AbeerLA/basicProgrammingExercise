
# Input student's score
score = int(input("Enter student's score: "))

def calculate_grade(score):
    if score >= 90 and score <= 100:
        return 'A'
    elif score >= 80 and score <= 89:
        return 'B'
    elif score >= 70 and score <= 79:
        return 'C'
    elif score >= 60 and score <= 69:
        return 'D'
    else:
        return 'F'

# Calculate and print the corresponding grade
print("Letter Grade:", calculate_grade(score))
