task = input("Enter you task: ")
time_bound = input("Is it time-bound? (yes or no) ").lower()
priority= input("Prioritys (high, medium, low): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority tasks that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task.")
        else:
            print(f"Note: '{task}' is not timebound. Consider completing it once you have time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task. It however requires you to allocate some time for it")
        else:
            print(f"Note: '{task}' is a low priority. Consider compelting it when you have free time.")
    case _:
        print("Invalid input, please enter a value withing the range provided.")