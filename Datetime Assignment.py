from datetime import datetime

start_date = input("Enter the start date YYYY-MM-DD: ")
end_date = input("Enter the end date YYYY-MM-DD: ")

start_date = datetime.strptime(start_date, "%Y-%m-%d")
end_date = datetime.strptime(end_date, "%Y-%m-%d")

if start_date > end_date:
    print("Invalid input")
else:
    
    current_date = start_date
    while current_date <= end_date:
        
        
        if current_date.weekday() < 5:
            task = input("Enter the task for {}: ".format(current_date.strftime('%A, %Y-%m-%d')))
            print("Task for {}: {}".format(current_date.strftime('%A, %Y-%m-%d'), task))
        else:
            print("{} is a weekend. No task assigned.".format(current_date.strftime('%A, %Y-%m-%d')))

        year, month, day = current_date.year, current_date.month, current_date.day
        if day < (datetime(year, month + (month == 12), 1) - datetime(year, month, 1)).days:
            current_date = datetime(year, month, day + 1)
        else:
            if month < 12:
                current_date = datetime(year, month + 1, 1)
            else:
                current_date = datetime(year + 1, 1, 1)
