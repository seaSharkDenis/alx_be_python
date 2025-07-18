task = input("Enter your task: ")
priority= input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = ""

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}'s' priority level is unkown"

if time_bound == "yes" and priority in ["high", "medium"]:
    reminder += " that requires immediate attention today!"
elif time_bound == "yes" and priority == "low":
    pass

print(f"Reminder: {reminder}")