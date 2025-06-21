import webbrowser

command = input("Enter your command: ")  # e.g., "huge search what is machine learning"

words = command.split(" ")  # ['huge', 'search', 'what', 'is', 'machine', 'learning']

if "google" in command.lower():
    query_words = words[2:]  # skip 'huge' and 'search'
    query = "+".join(query_words)  # 'what+is+machine+learning'
    
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
