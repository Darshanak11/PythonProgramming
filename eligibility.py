#cheakinng eligibility for the of student for the course
def check_eligibility(age, marks):
    if age<20 and marks>=65:
        return True
    else:
        return False
age = int(input("Enter the age: "))
marks = float(input("Enter the marks: "))
eligibility = check_eligibility(age, marks)
if eligibility:
    print("The student is eligible for the course.")
else:
    print("The student is not eligible for the course.")
