from ntpath import join


firstName = input("Enter your first name : ")
lastName = input("Enter your last name : ")
firstName = firstName[::-1]
lastName = lastName[::-1]
print(f"{lastName} , {firstName}")