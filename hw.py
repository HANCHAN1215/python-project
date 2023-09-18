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

