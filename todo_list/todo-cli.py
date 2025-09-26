import os
import sys
import datetime

TASK_FILE = "tasks.txt"


def get_task_id():
    new_id = 0

    tasks = load_tasks()
    if tasks:
        last_task = tasks[-1]
        print(f"Last Task: {last_task}")
        new_id = int(last_task.split("||")[0].split("-")[1].strip())+1
        print(f"Last ID: {new_id}")
    return f'{new_id:02d}'


def load_tasks() -> list:
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


def display_tasks_summary():
    tasks = load_tasks()
    pending_tasks = [task for task in tasks if task.endswith("pending")]
    high_priority_pending_tasks = [task for task in tasks if "High" in task and task.endswith("pending")]
    medium_priority_pending_tasks = [task for task in tasks if "Medium" in task and task.endswith("pending")]
    low_priority_pending_tasks = [task for task in tasks if "Low" in task and task.endswith("pending")]
    done_tasks = [task for task in tasks if task.endswith("done")]
    high_priority_done_tasks = [task for task in tasks if "High" in task and task.endswith("done")]
    medium_priority_done_tasks = [task for task in tasks if "Medium" in task and task.endswith("done")]
    low_priority_done_tasks = [task for task in tasks if "Low" in task and task.endswith("done")]
    print("-"*55+f"\n Task Summary\n"+('-')*55  )
    print(f"Total tasks: {len(tasks)}")
    print(f"\nPending tasks: {len(pending_tasks)}")
    print(f"{'  - High priority pending tasks':35} :\t{len(high_priority_pending_tasks)}")
    print(f"{'  - Medium priority pending tasks':<35} :\t{len(medium_priority_pending_tasks)}")
    print(f"{'  - Low priority pending tasks':<35} :\t{len(low_priority_pending_tasks)}")
    print(f"\nCompleted tasks: {len(done_tasks)}")
    print(f"{'  - High priority completed tasks':<35} :\t{len(high_priority_done_tasks)}")
    print(f"{'  - Medium priority completed tasks':<35} : \t{len(medium_priority_done_tasks)}")
    print(f"{'  - Low priority completed tasks':<35} :\t{len(low_priority_done_tasks)}")


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task+"\n")


def add_task(title,description, priotity="Low", deadline="No deadline"):
    tasks = load_tasks()
    new_id = get_task_id()
    tasks.append(f"task-{new_id}||{title}||{description}||{priotity}||{deadline}||pending")
    save_tasks(tasks)


def list_tasks(task_type="all"):
    tasks = load_tasks()
    filtered_tasks = []
    if task_type == "all":
        filtered_tasks = tasks
    if task_type == "pending":
        filtered_tasks = [task for task in tasks if task.endswith("pending")]
    if task_type == "done":
        filtered_tasks = [task for task in tasks if task.endswith("done")]
    
    if not filtered_tasks:
        print("No tasks found.")
        return
    
    print("-"*95+f"\n {'ID':<8}| {'Title':<20}| {'Description':<25}| {'Priority'} | {'Deadline':<12} | {'Status':<5} |\n"+('-')*95  )
    for index, task in enumerate(filtered_tasks):
        task_id,title,desc,priority,deadline, status = task.split("||")
        print(f" {task_id:<8}| {title:<20}| {desc:<25}| {priority:<8} | {deadline:<12} | {status:<5} |")
    print("-"*95)


def update_task(task_id):
    tasks = load_tasks()
    print(tasks, type(tasks))

    index = -1
    for s, task in enumerate(tasks):
        print(s, task)
        if task.startswith(task_id):
            index = s
            break
    if index == -1:
        print(f"Task ID {task_id} not found.")
        return
    print(f"Task Index to update: {index}")


    current_task_detail = tasks[index]
    task_desc = tasks[index]
    print(f"Selected Task Details: {current_task_detail}")
    while True:
        new_title = input("Enter new title (leave blank to keep current): ").strip()
        new_description = input("Enter new description (leave blank to keep current): ").strip()
        new_priority = input("Enter new priority (Low/Medium/High) (leave blank to keep current): ").strip().capitalize()

        while True:
            new_deadline = input("Enter new deadline (dd-mm-yyyy) (leave blank to keep current): ").strip()
            if new_deadline:
                try:
                    deadline_date = datetime.datetime.strptime(new_deadline, "%d-%m-%Y").date()
                    today = datetime.date.today()
                    if deadline_date >= today:
                        new_deadline = deadline_date.strftime("%d-%m-%Y")
                        break
                    else:
                        print("Deadline cannot be in the past. Please enter a valid date.")
                except ValueError:
                    print("Invalid date format. Please use dd-mm-yyyy format or press Enter for no deadline.")
            else:
                new_deadline = "No deadline"
                break

        new_status = input("Enter new status (pending/done) (leave blank to keep current): ").strip().lower()
        
        if new_title:
            task_desc = task_desc.replace(task_desc.split("||")[1], new_title)
        if new_description:
            task_desc = task_desc.replace(task_desc.split("||")[2], new_description)
        if new_priority in ["Low", "Medium", "High"]:
            task_desc = task_desc.replace(task_desc.split("||")[3], new_priority)
        if new_deadline:
            task_desc = task_desc.replace(task_desc.split("||")[4], new_deadline)
        if new_status in ["pending", "done"]:
            task_desc = task_desc.replace(task_desc.split("||")[5], new_status)
    
        if not (new_title or new_description or new_priority or new_deadline or new_status):
            print("No changes made. Please enter at least one field to update.")
        elif current_task_detail == task_desc:
            print("No changes detected. Please modify at least one field.")
        else:
            break

    tasks[index] = task_desc
    print(f"Updated Task Details: {task_desc}")

    save_tasks(tasks)


def delete_task(task_id):
    tasks = load_tasks()
    del tasks[task_id]
    save_tasks(tasks)


def show_help():
    print("Command Line ToDo List Help")
    print("\nCommands available: \n* add,\n* list,\n* update,\n* delete,\n* help\n* exit\n")
    print('\nExample to add a task : \nenter "add" command to add a new task\nEnter task title when prompted\nEnter task description when prompted and hit enter\n')
    print('\nExample to list tasks : \nenter "list all" command to list all tasks\n\nenter "list pending" command to list all pending tasks\n\nenter "list done" command to list all completed tasks')
    print('\nExample to mark a task as update : \nenter "update" command to mark the task as done\nEnter task ID when prompted and hit enter\n')
    print('\nExample to delete a task : \nenter "delete" command to delete a task\nEnter task ID when prompted and hit enter\n')
    print('\nExample to exit : \nenter "exit" command to exit the application\n')


def show_exit_message():
    print("\nThank you for using the ToDo List Application. Goodbye!\n")


def handle_command():
    command = input("Enter command: ").strip().lower()
    while command != "exit":
        if command == "add":
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            priority = input("Enter priority (Low/Medium/High): ").strip().capitalize()
            if priority not in ["Low", "Medium", "High"]:
                print("Invalid priority. Setting to 'Low' by default.")
                priority = "Low"

            while True:
                deadline = input("Enter deadline (dd-mm-yyyy) [optional]: ").strip()
                if deadline:
                    try:
                        deadline_date = datetime.datetime.strptime(deadline, "%d-%m-%Y").date()
                        today = datetime.date.today()
                        if deadline_date >= today:
                            deadline = deadline_date.strftime("%d-%m-%Y")
                            break
                        else:
                            print("Deadline cannot be in the past. Please enter a valid date.")
                    except ValueError:
                        print("Invalid date format. Please use dd-mm-yyyy format or press Enter for no deadline.")
                else:
                    deadline = "No deadline"
                    break

            add_task(title, description, priority, deadline)
            print("Task added successfully!")
        elif command.__contains__("list"):
            task_type = command.split("list")[-1].strip()
            if task_type in ["all", "pending", "done"]:
                list_tasks(task_type)
            else:
                print("Invalid list command. Use 'list all', 'list pending', or 'list done'.")
        elif command == "update":
            user_ip = input("Enter the numerical part of the task ID to update status: ").strip()
            if user_ip.isdigit():
                task_id = f'task-{user_ip}'
                update_task(task_id)
                print(f"Task ID - {task_id} updated!")
            else:
                print("Invalid task ID.")
        elif command == "delete":
            user_ip = input("Enter the numerical part of the task ID to update status: ").strip()
            if user_ip.isdigit():
                task_id = f'task-{user_ip}'
                delete_task(int(task_id))
                print(f"Task ID - {task_id} deleted successfully!")
            else:
                print("Invalid task ID.")
        elif command == "summary":
            display_tasks_summary()
        elif command == "help":
            show_help()
        else:
            print("Unknown command. Type 'help' for instructions.")
        command = input("\nEnter command: ").strip().lower()

    if command == "exit":
        show_exit_message()



def run():
    print("*"*50+"\n\tWelcome to the ToDo List Application!\n"+"*"*50)
    print("\nManage your tasks easily from the command line.")
    print("\nCommands available: \n* add,\n* list,\n* update,\n* delete,\n* summary\n* help\n* exit\n")
    print("\nType 'help' to see usage instructions.\n")
    print("Here is a summary of your tasks:\n")
    display_tasks_summary()
    print("\nLet's get started!\n")
    handle_command()



if __name__ == "__main__":
    run()