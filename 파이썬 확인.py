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
