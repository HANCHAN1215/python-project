#2023/9/12
print("제 이름은 한승찬이고 학번은 202310636입니다.")


#2023/9/18


#1
def rev_str(str):
    if len(str) <= 1:
        return str
   
    return rev_str(str[1:]) + str[0]

strings = ["abcde", "Come again, Forever young!", "Amore, Roma"]

for str in strings:
    reverse = rev_str(str)
    print(f"'{str}'을(를) 뒤집으면 '{reverse}'입니다.")


#2

def sum_of_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])

def main():
    while True:
        input_str = input("여러 개의 정수를 공백으로 구분하여 입력하세요 (done으로 종료): ")
        if input_str.lower() == "done":
            break
        
        input_values = input_str.split()  
    
        integer_list = []
        for value in input_values:
            try:
                num = int(value)
                integer_list.append(num)
            except ValueError:
                print(f"'{value}'는 올바른 정수가 아닙니다. 무시합니다.")
    
        total_sum = sum_of_list(integer_list)
        print(f"리스트의 합: {total_sum}")

if __name__ == "__main__":
    main()



#3
import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
    emails = re.findall(email_pattern, text)
    
    return emails

input_text = input("텍스트를 입력하세요: ")

extracted_emails = extract_emails(input_text)

print("추출된 이메일 주소:")
for email in extracted_emails:
    print(email)


#4

with open('mbox.txt', 'r') as file:
    lines = file.readlines()


rev_numbers = []
for line in lines:
    if 'New Revision :39772' in line:
        try:
            
            revision = int(line.split(': ')[1].strip())
            rev_numbers.append(revision)
        except ValueError:
            pass 

if rev_numbers:
    average_revision = sum(rev_numbers) / len(rev_numbers)
    print(f"Average: {average_revision:.2f}")
else:
    print("error")

#1 (2023/9/28 4주차 과제)
from tkinter import *

window = Tk()
window.title("동물 투표")


dog_image = PhotoImage(file="C:/Users/apple/OneDrive/바탕 화면/파이썬/새 폴더/dog.gif")
cat_image = PhotoImage(file="C:/Users/apple/OneDrive/바탕 화면/파이썬/새 폴더/cat.gif")
rabbit_image = PhotoImage(file="C:/Users/apple/OneDrive/바탕 화면/파이썬/새 폴더/rabbit.gif")

image_label = Label(window, image=None)
image_label.pack()

selected_animal_image = None

def vote(animal):
    global selected_animal_image
    print(f"당신은 {animal}을(를) 선택했습니다.")
    if animal == "강아지":
        selected_animal_image = dog_image
    elif animal == "고양이":
        selected_animal_image = cat_image
    elif animal == "토끼":
        selected_animal_image = rabbit_image

def show_image():
    if selected_animal_image:
        image_label.configure(image=selected_animal_image)
        image_label.image = selected_animal_image

for animal in ["강아지", "고양이", "토끼"]:
    radio_button = Radiobutton(window, text=animal, value=animal, command=lambda a=animal: vote(a))
    radio_button.pack()

show_image_button = Button(window, text="사진 보기", command=show_image)
show_image_button.pack()

window.mainloop()


#2

from tkinter import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
num = 0

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    label.config(text=fnameList[num])  

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    label.config(text=fnameList[num])  

window = Tk()
window.geometry("700x500")
window.title("Tk")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)


label = Label(window)
label.pack()
label.config(text=fnameList[num])  

window.mainloop()


#3
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