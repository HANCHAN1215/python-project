from tkinter import *

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)

app = Tk()
app.title("To-Do 리스트 관리 프로그램")

task_entry = Entry(app)
task_entry.pack(pady=10)

add_button = Button(app, text="Add Task", command=add_task)
add_button.pack()

delete_button = Button(app, text="Delete Task", command=delete_task)
delete_button.pack()

task_list = Listbox(app)
task_list.pack()

app.mainloop()
