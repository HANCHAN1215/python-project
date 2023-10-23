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

#(2023/10/16 5주차 과제)

import tkinter as tk
import sqlite3

conn = sqlite3.connect('md202310636.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user_data (
                    user_id INTEGER ,
                    username TEXT,
                    email TEXT,
                    birth_year INTEGER
                )''')
conn.commit()

def add_data():
    username = entry_username.get()
    email = entry_email.get()
    birth_year = entry_birth_year.get()
    
    if not (username and email and birth_year):
        result_label.config(text="데이터 입력 실패")
        return
    
    cursor.execute("INSERT INTO user_data (username, email, birth_year) VALUES (?, ?, ?)", (username, email, birth_year))
    conn.commit()
    entry_username.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_birth_year.delete(0, tk.END)
    result_label.config(text="데이터 입력 성공")

def show_data():
    user_id = entry_user_id.get()
    if user_id:
        cursor.execute("SELECT * FROM user_data WHERE user_id=?", (user_id,))
        data = cursor.fetchone()
        if data:
            result_label.config(text=f"사용자 ID: {data[0]}, 이름: {data[1]}, 이메일: {data[2]}, 출생 연도: {data[3]}")
        else:
            result_label.config(text="데이터가 없습니다.")
    else:
        cursor.execute("SELECT * FROM user_data")
        data = cursor.fetchall()
        if not data:
            result_label.config(text="데이터가 없습니다.")
        else:
            result = "\n".join([f"사용자 ID: {row[0]}, 이름: {row[1]}, 이메일: {row[2]}, 출생 연도: {row[3]}" for row in data])
            result_label.config(text=result)

window = tk.Tk()
window.title("데이터베이스 프로그램")

label_user_id = tk.Label(window, text="사용자 ID:")
label_username = tk.Label(window, text="이름:")
label_email = tk.Label(window, text="이메일:")
label_birth_year = tk.Label(window, text="출생 연도:")

entry_user_id = tk.Entry(window)
entry_username = tk.Entry(window)
entry_email = tk.Entry(window)
entry_birth_year = tk.Entry(window)

add_button = tk.Button(window, text="입력", command=add_data)
show_button = tk.Button(window, text="조회", command=show_data)

result_label = tk.Label(window, text="결과가 여기에 표시됩니다.")

label_user_id.grid(row=0, column=0)
label_username.grid(row=1, column=0)
label_email.grid(row=2, column=0)
label_birth_year.grid(row=3, column=0)

entry_user_id.grid(row=0, column=1)
entry_username.grid(row=1, column=1)
entry_email.grid(row=2, column=1)
entry_birth_year.grid(row=3, column=1)

add_button.grid(row=4, column=0)
show_button.grid(row=4, column=1)

result_label.grid(row=5, columnspan=2)

window.mainloop()

conn.close()

#(2023/10/23 6주차 과제)

#1
import queue

documents = {'A': 0, 'B': 2, 'C': 1, 'D': 1}

sorted_documents = sorted(documents.items(), key=lambda x: x[1], reverse=True)

stack = []
q = queue.Queue()

for document, importance in sorted_documents:
    q.put((document, importance))

while not q.empty():
    document, importance = q.get()
    print(f"{document}: 중요도 {importance}")

#2
from collections import deque

def find_price_changes(prices):
    n = len(prices)
    result = [-1] * n  

    stack = deque()  

    for i in range(n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        result[j] = n - j - 1

    return result

price = [3, 5, 2, 6, 1, 4, 7]

changes = find_price_changes(price)
for i, change in enumerate(changes):
    print(f"Price의 {i}번째 값은 {change}초 후에 떨어진다.")

#3
from collections import Counter

text_1 = "Python is a popular programming language. It is widely used for web development and data analysis. Machine learning and artificial intelligence are important topics in Python programming.".lower()
text_2 = "Java is another widely used programming language. It is known for its portability and versatility. Android app development can be done using Java programming.".lower()

words_1 = text_1.split()
words_2 = text_2.split()

word_count_1 = Counter(words_1)
word_count_2 = Counter(words_2)

for word in word_count_1.keys():
    count_1 = word_count_1[word]
    count_2 = word_count_2.get(word, 0)  
    print(f"'{word}': 파일1 - {count_1}, 파일2 - {count_2}")

for word in word_count_2.keys():
    if word not in word_count_1:
        count_1 = 0
        count_2 = word_count_2[word]
        print(f"'{word}': 파일1 - {count_1}, 파일2 - {count_2}")