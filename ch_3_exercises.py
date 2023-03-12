print("Financial Aid Eligibility Checker\n")

# Get student information

gpa = float(input("What is your current GPA? "))
criminal_record = input("Have you ever been convicted of a drug-related crime? ")
enrolled_credit_hours = int(input("How many credit hours do you plan to enroll in? "))
gross_income = float(input("What is your gross yearly income? "))

# Check eligibility
eligible = False
student_type='new'
if student_type.lower() == "new":
    eligible = True
elif gpa >= 2.0:
    eligible = True

if criminal_record.lower() == "no":
    eligible = True
else:
    eligible = False

if enrolled_credit_hours >= 6:
    eligible = True
else:
    eligible = False

if gross_income < 50000:
    eligible = True
else:
    eligible = False

# Display results
if eligible:
    print("Congratulations! You are eligible for financial aid for the next semester.")
else:
    print("Sorry, you are not eligible for financial aid for the next semester.")
