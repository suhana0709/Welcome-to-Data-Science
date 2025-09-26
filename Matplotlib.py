import matplotlib.pyplot as ptl

students_name=["Raju","Munna","Tom","Zarif","Suhana","Rudro","Jhon","Harry"]
students_marks=[23,49,12,50,0,1,2,45]

marks_perc=[]

for x in students_marks:
  res=(x/50)*100
  marks_perc.append(res)
print(marks_perc)

def line_chart_for_students_and_marks():
  ptl.plot(students_name,students_marks)
  ptl.title("Students marks graph")
  ptl.xlabel("Students name")
  ptl.ylabel("Students marks")
  ptl.show()

line_chart_for_students_and_marks()


def percentage_bar_chart():
  ptl.bar(students_name, marks_perc)
  ptl.title("Bar Graph for Student's Percentage")
  ptl.xlabel("Student's Names")
  ptl.ylabel("Student's Percentage")
  ptl.show()

percentage_bar_chart()