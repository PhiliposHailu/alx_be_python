task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task that requires your attention. Note that it is not time-bound.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: The task '{task}' is of {priority} priority. Do this task as soon as you have time to spare.")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Complete this task when you have some time. Note that it is not time-bound.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it in your free time, but note that it's a time-bound task.")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
