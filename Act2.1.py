english = float(input("Enter grade for English: "))
filipino = float(input("Enter grade for Filipino: "))
science = float(input("Enter grade for Science: "))
math = float(input("Enter grade for Math: "))
araling_panlipunan = float(input("Enter grade for Araling Panlipunan: "))
physical_education = float(input("Enter grade for Physical Education: "))

num_grades = 6
sum_grades = english + filipino + science + math + araling_panlipunan + physical_education
avg_grade = sum_grades / num_grades

print("The average grade is:", avg_grade)