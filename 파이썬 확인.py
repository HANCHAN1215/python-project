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

