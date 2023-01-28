class Student:
    amount_of_student = 0

    def __init__(self,height = 160):
        self.height = height
        Student.amount_of_student += 1

    def grow(self, height=1):
        self.height += height

nick = Student()
Kate = Student(height=175)
nick.grow(height=25)

print(Kate.height)
print(nick.height)
Kate.grow(height=20)
print(Kate.height)




st1 = Student()
st2 = Student()
# st3 = Student()
# st4 = Student()
# # print(st1.height)
# # print(st2.height)
# # print(st3.height)
# # print(Student.amout_of_students)
# # print(st1.amout_of_students)
# # print(st1.group)
# # print(st2.group)
# # print(st3.group)
# # print(st4.group)
# #
# # st1.group = "V 2925"
# # st2.group = "S 4040"
# # st3.group = "SP1215"
# # st4.group = "STEP"
# #
# #
# # print(st1.group)
# # print(st2.group)
# # print(st3.group)
# # print(st4.group)
# #
# # print(Student.group)