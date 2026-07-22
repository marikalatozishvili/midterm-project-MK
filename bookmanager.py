import json

# ფაილის სახელი, სადაც წიგნები ინახება
FILENAME = "books.json"

def load_books():
    # """ფუნქცია კითხულობს წიგნებს JSON ფაილიდან."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_books(books_list):
    # """ფუნქცია ინახავს წიგნების სიას JSON ფაილში."""
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(books_list, file, ensure_ascii=False, indent=4)

print("კეთილი იყოს თქვენი მობრძანება წიგნების მართვის აპლიკაციაში")

# პროგრამის ჩართვისას ვტვირთავთ წიგნებს ფაილიდან
books = load_books()

# უსასრულო ციკლი მენიუსთვის
while True:
    print("\nმთავარი მენიუ")
    print("1. ყველა წიგნის ნახვა")
    print("2. წიგნის დამატება")
    print("3. წიგნის განახლება")
    print("4. წიგნის წაშლა")
    print("5. პროგრამიდან გასვლა")
    
    choice = input("აირჩიეთ მოქმედება (1-5): ").strip()
    
    # თუ მომხმარებელმა უბრალოდ Enter დააჭირა და არაფერი შემოიტანა, თავიდან ვატრიალებთ ციკლს ყოველგვარი შეცდომის დაბეჭდვის გარეშე
    if not choice:
        continue
    
    # 1. წიგნების ნახვა 
    if choice == '1':
        if not books:
            print("ბიბლიოთეკა ამჟამად ცარიელია.")
        else:
            print("\nწიგნების სია:")
            for index, book in enumerate(books, start=1):
                print(f"{index}. სათაური: {book['title']} | ავტორი: {book['author']}")
                32

    # 2. წიგნის დამატება 
    elif choice == '2':
        title = input("შეიყვანეთ წიგნის სათაური: ").strip()
        author = input("შეიყვანეთ ავტორი: ").strip()
        
        if title and author:
            new_book = {"title": title, "author": author}
            books.append(new_book)
            save_books(books)
            print(f"წიგნი '{title}' წარმატებით დაემატა და შეინახა.")
        else:
            print("შეცდომა: სათაური და ავტორი არ უნდა იყოს ცარიელი.")
            
    # 3. წიგნის განახლება 
    elif choice == '3':
        if not books:
            print("ბიბლიოთეკა ცარიელია, განახლება შეუძლებელია.")
        else:
            print("\nარსებული წიგნები:")
            for index, book in enumerate(books, start=1):
                print(f"{index}. სათაური: {book['title']} | ავტორი: {book['author']}")
                
            try:
                book_num = int(input("შეიყვანეთ იმ წიგნის ნომერი, რომლის განახლებაც გსურთ: "))
                if 1 <= book_num <= len(books):
                    selected_book = books[book_num - 1]
                    
                    print(f"მიმდინარე მონაცემები -> სათაური: {selected_book['title']}, ავტორი: {selected_book['author']}")
                    
                    new_title = input("შეიყვანეთ ახალი სათაური (ან დატოვეთ ცარიელი უცვლელად): ").strip()
                    new_author = input("შეიყვანეთ ახალი ავტორი (ან დატოვეთ ცარიელი უცვლელად): ").strip()
                    
                    if new_title:
                        selected_book['title'] = new_title
                    if new_author:
                        selected_book['author'] = new_author
                        
                    save_books(books)
                    print("წიგნის მონაცემები წარმატებით განახლდა.")
                else:
                    print("შეცდომა: ასეთი ნომრით წიგნი არ არსებობს.")
            except ValueError:
                print("შეცდომა: გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")
                
    # 4. წიგნის წაშლა 4

    elif choice == '4':
        if not books:
            print("ბიბლიოთეკა ცარიელია, წაშლა შეუძლებელია.")
        else:
            print("\nარსებული წიგნები:")
            for index, book in enumerate(books, start=1):
                print(f"{index}. სათაური: {book['title']} | ავტორი: {book['author']}")
                
            try:
                book_num = int(input("შეიყვანეთ იმ წიგნის ნომერი, რომლის წაშლაც გსურთ: "))
                if 1 <= book_num <= len(books):
                    removed_book = books.pop(book_num - 1)
                    save_books(books)
                    print(f"წიგნი '{removed_book['title']}' წარმატებით წაიშალა.")
                else:
                    print("შეცდომა: ასეთი ნომრით წიგნი არ არსებობს.")
            except ValueError:
                print("შეცდომა: გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")
                
    # 5. პროგრამიდან გასვლა
    elif choice == '5':
        print("პროგრამა დასრულდა. ნახვამდის.")
        break
        
    else:
        print("არასწორი არჩევანი. გთხოვთ შეიყვანოთ რიცხვი 1-დან 5-მდე.")ს