task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task that reuires immediate attention today!")
        else:
            print(f"'{task}' is a {priority} priority task that reuires your attention. note that it is not time bound.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task. complete this task as soon as you have time to spare.")
        else:
            print(f"'{task}' is a {priority} priority task. complete this task when you got some time.note that it is not time bounded.")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task. Consider completing it in your free time but note that it's a time bound task.")
        else:
            print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")

