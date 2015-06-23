#!/bin/python2.7
# codecademy - Python
# Gradebook

# Define Student Names
student1 = raw_input(“Enter name of Student 1: “)
student2 = raw_input(“Enter name of Student 2: “)
student3 = raw_input(“Enter name of Student 3: “)

# Create Dictionary for Each Student
student1 = {
    "name" : "student1", 
    "homework" : [], 
    "quizzes" : [], 
    "tests" : []
}
student2 = {
    "name" : "student2",
    "homework" : [], 
    "quizzes" : [], 
    "tests" : []
}
student3 = {
    "name" : "student3", 
    "homework" : [], 
    "quizzes" : [], 
    "tests" : []
}

# Define Grades
print “Issue grades with one(1) decimal point \”94.0\” rather than \”94\””

print “Grades for “ + student1
s1h1 = int(input(“Homework 1: “)
s1h2 = int(input(“Homework 2: “)
s1h3 = int(input(“Homework 3: “)
s1h4 = int(input(“Homework 4: “)
s1q1 = int(input(“Quiz 1: “)
s1q2 = int(input(“Quiz 2: “)
s1q3 = int(input(“Quiz 3: “)
s1t1 = int(input(“Test 1: “)
s1t2 = int(input(“Test 2: “)

print “Grades for %s“ + student2
s2h1 = int(input(“Homework 1: “)
s2h2 = int(input(“Homework 2: “)
s2h3 = int(input(“Homework 3: “)
s2h4 = int(input(“Homework 4: “)
s2q1 = int(input(“Quiz 1: “)
s2q2 = int(input(“Quiz 2: “)
s2q3 = int(input(“Quiz 3: “)
s2t1 = int(input(“Test 1: “)
s2t2 = int(input(“Test 2: “)

print “Grades for “ + student1
s3h1 = int(input(“Homework 1: “)
s3h2 = int(input(“Homework 2: “)
s3h3 = int(input(“Homework 3: “)
s3h4 = int(input(“Homework 4: “)
s3q1 = int(input(“Quiz 1: “)
s3q2 = int(input(“Quiz 2: “)
s3q3 = int(input(“Quiz 3: “)
s3t1 = int(input(“Test 1: “)
s3t2 = int(input(“Test 2: “)

student1 = {
    "name" : "student1",
    "homework" : [s1h1, s1h2, s1h3, s1h4],
    "quizzes" : [s1q1, s1q2, s1q3],
    "tests" : [s1t1, s1t2]
}

student2 = {
    "name" : "student2",
    "homework" : [s2h1, s2h2, s2h3, s2h4],
    "quizzes" : [s2q1, s2q2, s2q3],
    "tests" : [s2t1, s2t2]
}
student3 = {
    "name" : "student3",
    "homework" : [s3h1, s3h2, s3h3, s3h4],
    "quizzes" : [s3q1, s3q2, s3q3],
    "tests" : [s3t1, s3t2]
}

# List Student Names
students = [student1, student2, student3]
print students

# Print Each Student’s Name and Grades
for student in students:
    print student["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]

# Division in python
## 5 / 2 ---> 2
## 5.0 / 2 ---> 2.5
## float(5) / 2 ---> 2.5

def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

# Weighted Averages
# "\" is used as a continuation -> stuff to the right is considered a continuation of what's on the left

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return (homework * 0.1) + (quizzes * 0.3) + (tests * 0.6)

# Letter Grades
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print get_letter_grade(get_average(student1))
# Class Averages
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
print get_class_average(students)