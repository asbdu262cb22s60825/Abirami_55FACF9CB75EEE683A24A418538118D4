def sort_students(student_list):
  sorted_students=sorted(student_list,key=lambda x:x.cgpa,reverse=True)
  return sorted_students

class student:
  def_init_(self,name,roll_number,cgpa):
   self.name=name
   self.roll_number=roll_number
   selfself.cgpa=cgpa

#Example usage:
students=[
  student("Alice","A123",3.8),
  student("Bob","B456",3.9),
  student("charlie","C789",3.7)
]

sorted_studentsort_students(students)
for student in sorted_students:
  printf("Name:{student.name},Roll Number:{student.roll_number},CGPA:{student.cgpa}")