"""
  The function allows users to manage tasks by adding, updating, deleting, viewing, and exiting tasks
  in a task management app.
  """

def tasks():

  task = []
  print("___Welcome to task management app___")
  total_task = int(input("Enter how many task you want to add = "))
  for i in range(1,total_task+1):
    task_name=input(f"Enter task {i}=")
    task.append(task_name)
  
  print(f"Today's task are\n{task}")
  
  while True:
    operation =int(input("Enter\n1 for Add\n2 for Update\n3 for Delete\n4 for View\n5 for Exit/stop"))
    
    if operation == 1:
      add=input("enter task you want to add")
      task.append(add)
      print(f"Task {add} has successfully added.")
      
    elif operation==2:
      update_val =input("Enter the task name you want to update=")
      if update_val in task:
        up=input("Enter new task")
        ind =task.index(update_val)
        task[ind]=up
        print(f"Update task {up}")
      else:
        print("Task not found")
        
    elif operation ==3:
      delete_val=input("Enter task you want to delete:")
      if delete_val in task:
        task.remove(delete_val)
        print(f"Task{delete_val} delete successfully")
      else:
        print("Task not found")
    
    elif operation==4:
      print(f"total task={task}")
      
        
    elif operation == 5:
      print("Exiting...")
      break
    
tasks()