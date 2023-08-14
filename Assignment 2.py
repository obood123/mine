import datetime
Employee=[]
class Employees :
    def __init__(self,D):
          self.D=D    
    def Save_Employee(self):
          Employee.append(self.D)
          return(Employee)                    
    def Create_Employees(Dic):
        Employe=Dic
        return Employe   
    def Update_Employee(e,di):
     if(di=={'emp_id':'','name':'','joining_date':datetime.date(1,1,1),'salary':''}):
            return Employee
     else:  
        d=len(Employee)-1
        while d>=0:
         if (e==Employee[d]['emp_id']):
            Employee[d]=di
            break
         else:
                 d-=1
    def Delete_Employee(r):
        d=len(Employee)-1
        while d>=0:
         if (r==Employee[d]['emp_id']):
            Employee.pop(d)
            break
         else:
                 d-=1
    def Search_Employee():
     v=input("Do you want to search about certain employee? ")   
     if(v=='yes' or v=='Yes'or v== 'Y' or v=='y'):
      a=int(input('Enter ID for employee you search about him : '))
      b=input('Enter Name for employee you search about him : ')
      d=len(Employee)-1
      while d>=0:
       if (a==Employee[d]['emp_id'] or b==Employee[d]['name']):
        print (f"His ID is: {Employee[d]['emp_id']}, His name is: {Employee[d]['name']}, His joining date is: {Employee[d]['joining_date']}, His salary is: {Employee[d]['salary']}")
        break
       else:
         d-=1
      else:
            print('There is no one with this ID and name') 
     else:
         pass 
    def Sort_Employees():
        v=input("Do you want to sort the employees? ")   
        if(v=='yes' or v=='Yes'or v== 'Y' or v=='y'):
            z=input("Choose one of the following sort criterias : id, name, joining date, salary : ")
            if(z=='id'):
                print('Employees sorting by ID :')
                l=[]
                k=len(Employee)-1
                for i in range(0,k+1): 
                 l.append(Employee[i]['emp_id'])
                 l.sort()
                u=len(l)-1
                for i in range(0,u+1):
                    for j in range(0,k+1):
                        if(Employee[j]['emp_id']==l[i]):
                            print(Employee[j])
            elif(z=='name'):
                print('Employees sorting by Name :')
                l=[]
                k=len(Employee)-1
                for i in range(0,k+1): 
                 l.append(Employee[i]['name'])
                 l.sort()
                u=len(l)-1
                for i in range(0,u+1):
                    for j in range(0,k+1):
                        if(Employee[j]['name']==l[i]):
                            print(Employee[j])
            elif(z=='joining date'):
                print('Employees sorting by Joining date :')
                l=[]
                k=len(Employee)-1
                for i in range(0,k+1): 
                 l.append(Employee[i]['joining_date'])
                 l.sort()
                u=len(l)-1
                for i in range(0,u+1):
                    for j in range(0,k+1):
                        if(Employee[j]['joining_date']==l[i]):
                            print(Employee[j])
            elif(z=='salary'):
                print('Employees sorting by Salary :')
                l=[]
                k=len(Employee)-1
                for i in range(0,k+1): 
                 l.append(Employee[i]['salary'])
                 l.sort()
                u=len(l)-1
                for i in range(0,u+1):
                    for j in range(0,k+1):
                        if(Employee[j]['salary']==l[i]):
                            print(Employee[j])
            else:
                print("Wrong insertion") 
        else:
            pass            
    def create():
     a=4
     s=int(input("How many employees do you want to create them : ")) 
     global emp 
     emp={'emp_id':'','name':'','joining_date':datetime.date(1,1,1),'salary':''}    
     while s>0:
        emp['emp_id']=a
        emp['name']=input('Enter name of employee: ').capitalize()
        emp['joining_date']=input('Enter joining date of employee: ')
        while True :
            try:
             emp['salary']=int(input('Enter salary of employee: '))
             break
            except:
             print('incorrect number')
        s-=1   
        a+=1
        Employee.append(emp)
        emp={'emp_id':'','name':'','joining_date':datetime.date(1,1,1),'salary':''} 
    def update():
     global emps 
     emps={'emp_id':'','name':'','joining_date':datetime.date(1,1,1),'salary':''}  
     n=input("What is name of employee you need to update him : ")  
     d=len(Employee)-1
     while d>=0:
          if (n==Employee[d]['name']):
            emps['emp_id']=Employee[d]['emp_id']
            emps['name']=input('Enter name of employee: ').capitalize()
            emps['joining_date']=input('Enter joining date of employee: ')
            while True :
             try:
              emps['salary']=int(input('Enter salary of employee: '))
              break
             except:
              print('incorrect number')
            break
          else:
             d-=1
     else:
            print('There is no one with this name')         
    def delete():
     global empa 
     empa={'emp_id':''}  
     b=input("What is the name of an employee you need to delete him :")
     f=len(Employee)-1
     while f>=0:
      if (b == Employee[f]['name']):
             empa['emp_id']=Employee[f]['emp_id']
             break  
      else:
         f-=1
     else:      
                print('There is no one with this name') 
one=Employees({'emp_id':1,'name':'Ali','joining_date':str(datetime.date(2022,2,1)),'salary':2000})  
one.Save_Employee()  
one=Employees({'emp_id':2,'name':'Ahmed','joining_date':str(datetime.date(2022,2,15)),'salary':1500})  
one.Save_Employee() 
one=Employees({'emp_id':3,'name':'Omar','joining_date':str(datetime.date(2022,3,1)),'salary':1000})  
one.Save_Employee()          
Employees.create()
Employees.Create_Employees(Employee)
Employees.update()
Employees.Update_Employee(emps['emp_id'],emps) 
Employees.delete()     
Employees.Delete_Employee(empa['emp_id'])   
Employees.Search_Employee()     
Employees.Sort_Employees()           