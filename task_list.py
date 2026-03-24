import os
ex='__To-do-list __'
print(ex.center(50))

record={}



def view_task():
      with open("task.txt","r")as file:
          content=file.read()
          print(content)


def save_exit():
    with open("task.txt", "w") as file:
        for name, desc in record.items(): 
            file.write( name + "," + str(desc) + "\n")
    print(" Task Saved successfully")           

def delete_task():
     item = input("Enter task  to delete: ")
     try:
         with open("task.txt", "r") as file:
             lines = file.readlines()
         
         new_lines = []
         deleted = False
         for line in lines:
             name, desc = line.strip().split(",")
             if name.strip() != item.strip():
                 new_lines.append(line)
             else:
                 deleted = True
         
         if deleted:
             with open("task.txt", "w") as file:
                 file.writelines(new_lines)
             print(f"{item} deleted successfully")
             if item in record:
                 del record[item]
         else:
             print(f"Item '{item}' not found in records.")
     except FileNotFoundError:
         print("No record file found.")
     except ValueError:
         print("Error parsing record file.") 

def load_task():
    global record
    try:
        with open("task.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, desc = parts
                    record[name] = desc
    except FileNotFoundError:
        pass
    except ValueError:
        print("Error loading some records.")
load_task()   

def show():
    print("Option 1: Add task")
    print("Option 2: View task")
    print("Option 3: Save and Exit")
    print("Option 4: Delete task")

 

while True:
     show()
     choice=int(input("choose a option from 1 to 5 :"))
     if (choice==1) :
          def add_task(name,desc):
             record[name]=desc
          name=input("Enter task name:")
          desc=input("Enter task description:") 
          add_task(name,desc)
     
     elif (choice==2) : 
        view_task()   
     elif (choice==3) :
        save_exit()
        break   
     elif (choice==4):
        delete_task()
     else:
         print("enter valid choice")