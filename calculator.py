
print("--- Welcome to Mari's Calculator ---")

# ვიწყებთ უსასრულო ციკლს, რომელიც საშუალებას მოგვცემს გავაგრძელოთ გამოთვლები ან გავაჩეროთ პროგრამა
while True:
    
    # 1. თავიდან ვეკითხებით გვინდა თუ არა გაგრძელება, თუ არა ვაჩერებთ პროგრამას. თან ვაშოორებტ ერთი ხაზით 
    action = input("\nDo you want to calculate? (Type 'yes' to continue, 'no' to quit): ")
    
    if action == 'no':
        print("Calculator is off. Bye!")
        break  
        
    # 2. უსასრულო ციკლის შიგნით ვიყენებთ try-except ბლოკს, რათა დავიჭიროთ შეცდომები, რომლებიც შეიძლება წარმოიშვას მომხმარებლის შეყვანის დროს.
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /, **): ")
        num2 = float(input("Enter the second number: "))

        # 3. შემდეგ ვამოწმებთ ოპერაციას და ვასრულებთ შესაბამის გამოთვლას.
        if operation == '+':
            result = num1 + num2
            print("Result:", result)
        elif operation == '-':
            result = num1 - num2
            print("Result:", result)
        elif operation == '*':
            result = num1 * num2
            print("Result:", result)
        elif operation == '/':
            result = num1 / num2
            print("Result:", result)
        elif operation == '**':
            result = num1 ** num2
            print("Result:", result)
        else:
            print("Error: Invalid operation!")
            
    # 4. თუ მომხმარებელი შეიყვანა არასწორი მონაცემები (მაგალითად, ტექსტი რიცხვის ნაცვლად), ან სცადა ნულის გაყოფა, ჩვენ ვაჩვენებთ შესაბამის შეცდომის შეტყობინებას.
    except ValueError:
        print("Error: You must enter a valid number, not text.")
    except ZeroDivisionError:
        print("Error: You cannot divide a number by zero.")