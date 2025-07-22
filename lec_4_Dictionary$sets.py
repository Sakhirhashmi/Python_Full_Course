# student = {
#     "name": "sakhir hashmi",
#     "Age": "23",
#     "degree": "Bs(information technology)",
#     "subjects": {
#         "Subject1": "Programming Fundamentals",
#         "Subject2": "OOP",
#         "Subject3": "DSA"
#     }
# }

# # Dictionary methods

# # return all keys
# print(student)

# # return all vaalues
# print(student["subjects"])
# print(list(student.values()))

# # reetur all the (key. value) pairsa just like tuple
# print(student.items())

# #  return the key according to the valu
# print(student.get("name"))  

# # update insert the specied item in the dictionary 
 
# student.update({"name": "sakhir ijaz"})
# print(student)


# Sets in python 

# collection = {1, 2, 3, 4,5,55,3, 9, 22, 10}
# clc = {2, 3, 4, 6}
# # collection.add(23)
# # collection.remove(55)
# # # collection.clear()
# # collection.pop()

# print(collection.union(clc))
# print(collection.intersection(clc))

# print(collection)


#  Practice excercise of sets and dictionary 

# 1 store the following value word meaning in the python dixtionart

# store = {
#     "table":["a piece of furniture", "list of facts & figure"],
#     "cat" : "A small animal"
# }

# print(store)

# 2 list of a subject find out the class room for differnt subject 

# subjects = {
#     "Python","java", "c++", "python", "js", "java", "python", "java", "c++", "c"
#     }
# print(len(subjects))
 


#   take the 3 marks input from the user and store them into the empty dictionary add one by one with subject name and value 


marks = {}

a = int (input("Physic Marks: "))
marks.update({"physcic" : a})

b= int (input("chem Marks: "))
marks.update({"chem" : b})

c = int (input("math Marks: "))
marks.update({"math" : c})

print(marks)