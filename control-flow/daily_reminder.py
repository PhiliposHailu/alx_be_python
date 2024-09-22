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
