# cheaking the student is  pass or not 
def check_persentage(marks):
     if marks>=65:
         return True
     else:
         return False
     
marks = float(input("Enter the marks: "))
persentage = check_persentage(marks)
if persentage:
        print("The student is passed.")
else:
        print("The student is fail.");