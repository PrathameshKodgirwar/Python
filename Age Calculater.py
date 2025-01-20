from datetime import datetime
bday_input = input("Enter Birthdate in yyyy-mm-dd format: ")
bday = datetime.strptime(bday_input, "%Y-%m-%d")
    
today = datetime.now()
    
age = today.year - bday.year
    
if (today.month, today.day) < (bday.month, bday.day):
    age -= 1
    
    print(f"Your age is: {age}")