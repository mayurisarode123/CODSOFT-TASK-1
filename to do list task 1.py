from tkinter import *
top=Tk()
top.config(bg="yellow")
top.geometry("500x400")
top.title("CODSOFT TASK 1")
tasks=[]
def new_task():
    task=e1.get()
    if task !="":
        tasks.append(task)
        e1.delete(0,END)
        update_tasks()
def update_tasks():
    task_list.delete(0,END)
    for task in tasks:
        task_list.insert(END,task)
def delete_tasks():
    selected_task=task_list.curselection()[0]
    del tasks[selected_task]
    update_tasks()
def exit():
       top.destroy()

l1=Label(top,text="WELCOME TO TO DO LIST",font="time 15",relief="sunken")
l1.pack()
l1=Label(top,text="ENTER A TASK TO BE ADDED",fg="black", font=('times'))
l1.pack(padx=10,pady=20)
e1=Entry(top)
e1.pack()


b1=Button(top,text="ADD TASK",
          font=('times 14'),
          bg='#c5f776',
          command=new_task,
          )
b1.pack(pady=22)

b2=Button(top,text="DELETE TASK",
          command=delete_tasks,
          font=('times 14'),
          bg='#ff8b61',
         
          )
b2.pack()
b3=Button(top,text="EXIT",command=exit,bg="blue",font="time 15")
b3.pack()
b3.place(x=350,y=300)
frame = Frame(top)
frame.pack(pady=5)
task_list=Listbox(top)

task_list.pack()

top.mainloop()

