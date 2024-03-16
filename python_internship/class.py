# class age:
#     X=5
# p1=age()
# print(p1.X)
# 
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("farisha",18)
# print(p1.name)
# print(p1.age)
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
# p1=Student("farisha",10)
# print(p1.name)
# print(p1.marks)
# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def make_sound(self):
#         return"woof"
# d1=Dog("jack")
# print(d1.name)
# print(d1.make_sound())
class Brands:
    brand_name_1="Amazon"
    brand_name_2="ebay"
class Products:
    prod_1="online ecommerce store"
    prod_2="online store"
class Popularity(Brands,Products):
    prod_1_popularity = 100
    prod_2_popularity = 70
obj_1= Popularity()
print(obj_1.brand_name_1 +"is an"+obj_1.prod_1+" is ",obj_1.prod_1_popularity)
print(obj_1.brand_name_2 +"is an"+obj_1.prod_2+" is ",obj_1.prod_2_popularity)