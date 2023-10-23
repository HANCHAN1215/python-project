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
