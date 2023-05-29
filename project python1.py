#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Student:
    pass


# In[25]:


class Student:
    def __init__(self,rollnumber,name,marks1,marks2):
        self.rollnumber=rollnumber
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        
        
    def display(self):
        print("Roll Number:",self.rollnumber)
        print("Name :",self.name)
        print("Marks1 :",self.marks1)
        print("marks2 :",self.marks2)
        
        
        
     
       


class StudentDatabase:
    def __init__(self):
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
    def search_student(self,rollno):
        for students in self.students:
            if student.rollno == rollno:
                return student
            return None
        
             
           
        

    
    def delete_student(self,rollno):
        student=self.search_student(rollno) 
        if student:
            self.students.remove(student)
            print("student data deleted successfully")
        else:
            print("student data not found")
            
#creating a student data system object
database=StudentDatabase()
#creating object
student1 = Student(1,"Aman",2,95)
student2 = Student(2,"Amit",85,88)
student3 = Student(3,"Suraj",72,78)
student4 = Student(4,"Naincy",60,64)
student5 = Student(5,"Daisy",54,52)


               
        
         
            
            
                
# displaying the student data
student1.display()
print()
student2.display()
print()
student3.display()
print()
student4.display()
print()
student5.display()
print()
    


#searching for a student    
roll_no=6
found_student=database.search_student(roll_no)
    
    
if found_student:
    print("student found")
    found_student.display()
else:
    print("student not found")
       
        
#to delete student data
rollno=8
database.delete_student(rollno)
print()
    

                     
                   
    


# In[ ]:




