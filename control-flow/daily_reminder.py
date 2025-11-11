user_task_description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound (yes or no): ")

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"'{user_task_description}' is a high priority task that requires immediate attention today!")
    case 'medium':
        print(f"'{user_task_description}' is a medium priority task. Consider completing it when you have free time.")
    case 'low':
        print(f"'{user_task_description}' is a low priority task. Consider completing it when you have free time.")


