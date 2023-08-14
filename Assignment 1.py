import datetime
a={'emp_id':1,'name':'Ali','joining_date':str(datetime.date(2022,2,1)),'salary':int('2000'),'department':'Back-end'}
b={'emp_id':2,'name':'Ahmed','joining_date':str(datetime.date(2022,2,15)),'salary':int('1500'),'department':'Back-end'}
c={'emp_id':3,'name':'Omar','joining_date':str(datetime.date(2022,3,1)),'salary':int('1000'),'department':'Front-end'}
Employees=[a,b,c]
def List_all_employees():
   print('List Of Employees : ')  
   print("ID  Name  Joining Date  Salary  Department : ")
   k=len(Employees)-1
   for i in range(0,k+1):
        li=[]
        li=Employees[i]
        print(*li.values())       
List_all_employees() 
def View_employee_by_id ():  
    while True :
        try:
            a=int(input("What is the ID of an employee you need to view him : "))
            break
        except:
             print('incorrect number')
    d=len(Employees)-1
    while d>=0:
     if (a==Employees[d]['emp_id']):
      print (f"His ID is: {Employees[d]['emp_id']}, His name is: {Employees[d]['name']}, His joining date is: {Employees[d]['joining_date']}, His salary is: {Employees[d]['salary']}, His department is :{Employees[d]['department']}")
      break
     else:
         d-=1
    if (a!=Employees[d]['emp_id']):
            print('There is no one with this ID')  
View_employee_by_id ()
def Create_employee():
      z=4
      s=int(input("How many employees do you want to create them : ")) 
      global emp 
      emp={'emp_id':'','name':'','joining_date':datetime.date(1,1,1),'salary':'','department':''}    
      while s>0:
        emp['emp_id']=z
        emp['name']=input('Enter name of employee: ').capitalize()
        emp['joining_date']=input('Enter joining date of employee: ')
        while True :
            try:
             emp['salary']=int(input('Enter salary of employee: '))
             break
            except:
             print('incorrect number')
        emp['department']=input('Enter department of employee: ')
        s-=1
        z+=1
        Employees.append(emp)
        emp={'emp_id':'','name':'','joining_date':datetime.date(1,1,1),'salary':'','department':''}  
Create_employee() 
def Update_employee():
 s=int(input("How many employees do you want to update them : ")) 
 while s>0:
  b=input("What is the name of an employee you need to update his data :")
  f=len(Employees)-1
  while f>=0:
    if (b == Employees[f]['name']):
         n=Employees[f]['emp_id']
         Employees.pop(f)
         global emp 
         emp={'emp_id':'','name':'','joining_date':datetime.date(1,1,1),'salary':'','department':''}  
         emp['emp_id']=n
         emp['name']=input('Enter new name of employee: ').capitalize()
         emp['joining_date']=input('Enter new joining date of employee: ')
         while True :
            try:
             emp['salary']=int(input('Enter new salary of employee: '))
             break
            except:
             print('incorrect number')
         emp['department']=input('Enter new department of employee: ')
         s-=1
         Employees.append(emp)
         emp={'emp_id':'','name':'','joining_date':datetime.date(1,1,1),'salary':'','department':''}  
         break
    else:
     f-=1 
  else: 
       if (b != Employees[f]['name']):
                  print('There is no one with this name')  
                  break    
Update_employee()     
def Delete_employee():
 s=int(input("How many employees do you want to delete them : ")) 
 f=len(Employees)-1
 while s>0:
  b=input("What is the name of an employee you need to delete his data :")
  while f>=0:
    if (b == Employees[f]['name']):
         Employees.pop(f)
         s-=1
         break  
    else:
         f-=1
  else:      
         if (b != Employees[f]['name']):
                print('There is no one with this name') 
                break 
Delete_employee() 
def Searching_by_emp_id_and_name():
    while True :
        try:
            a=int(input('Enter ID for employee you search about him :'))
            break
        except:
             print('incorrect number')
    b=input('Enter Name for employee you search about him :')
    d=len(Employees)-1
    while d>=0:
     if (a==Employees[d]['emp_id'] and b==Employees[d]['name']):
      print (f"His ID is: {Employees[d]['emp_id']}, His name is: {Employees[d]['name']}, His joining date is: {Employees[d]['joining_date']}, His salary is: {Employees[d]['salary']}, His department is :{Employees[d]['department']}")
      break
     else:
         d-=1
    if (a!=Employees[d]['emp_id'] and b!=Employees[d]['name']):
            print('There is no one with this ID or name')     
Searching_by_emp_id_and_name() 
def employees_sorting():
    print('Employees sorting by ID :')
    l=[]
    k=len(Employees)-1
    for i in range(0,k+1): 
            l.append(Employees[i]['emp_id'])
            l.sort()
    u=len(l)-1
    for i in range(0,u+1):
                    for j in range(0,k+1):
                        if(Employees[j]['emp_id']==l[i]):
                            print(Employees[j])
    print('Employees sorting by Name :')
    l=[]
    k=len(Employees)-1
    for i in range(0,k+1): 
            l.append(Employees[i]['name'])
            l.sort()
    u=len(l)-1
    for i in range(0,u+1):
                    for j in range(0,k+1):
                        if(Employees[j]['name']==l[i]):
                            print(Employees[j])
employees_sorting()
def Employees_report():
    print('Employees report:')
    print("Emp ID, Name, Joining Date, Department, Salary")
    k=len(Employees)-1
    for i in range(0,k+1):
        print(f"{Employees[i]['emp_id']}, {Employees[i]['name']}, {Employees[i]['joining_date']}, {Employees[i]['department']}, {Employees[i]['salary']}")   
Employees_report()  
def get_total_salaries_for_each_department ():
    total=0
    int(total)
    print('Department name, Total Salaries')
    k=len(Employees)-1
    for i in range(0,k+1):
     if (Employees[i]['department']=='Back-end'):
      a=Employees[i]['salary'] 
      total+=a  
    print (f"Back-end, {total}")
    k=len(Employees)-1
    total=0
    int(total)
    for i in range(0,k+1):    
     if (Employees[i]['department']=='Front-end'):
      a=Employees[i]['salary'] 
      total+=a  
    print (f"Front-end, {total}")
get_total_salaries_for_each_department ()    
def Get_first_and_last_employee_joined():
    b=Employees[0]['joining_date']  
    s=Employees[0]['joining_date'] 
    k=len(Employees)-1
    for i in range(0,k+1):
        if((Employees[i]['joining_date'])<s):
            s=Employees[i]['joining_date']
        if(s==Employees[i]['joining_date']):
            n=Employees[i]['name']     
    print(f"The first employee joined is: {n} ,and his joining date is: {s}")
    k=len(Employees)-1
    for i in range(0,k+1):
        if((Employees[i]['joining_date'])>b):
            b=Employees[i]['joining_date']  
        if(b==Employees[i]['joining_date']):
            v=Employees[i]['name']    
    print(f"The last employee joined is: {v} ,and his joining date is: {b}")  
Get_first_and_last_employee_joined() 
def Get_employee_with_low_and_high_salary():
    b=Employees[0]['salary']  
    s=Employees[0]['salary'] 
    k=len(Employees)-1
    for i in range(0,k+1):
        if((Employees[i]['salary'])<s):
            s=Employees[i]['salary']
        if(s==Employees[i]['salary']):
            n=Employees[i]['name']     
    print(f"employee with low salary is: {n} ,and his salary is: {s}")
    k=len(Employees)-1
    for i in range(0,k+1):
        if((Employees[i]['salary'])>b):
            b=Employees[i]['salary']  
        if(b==Employees[i]['salary']):
            v=Employees[i]['name']    
    print(f"employee with high salary is: {v} ,and his salary is: {b}")  
Get_employee_with_low_and_high_salary()  