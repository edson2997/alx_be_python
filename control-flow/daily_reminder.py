task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Make sure to schedule it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that needs to be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to complete it in the next few days.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task, but still time-sensitive. Try to get it done today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
        