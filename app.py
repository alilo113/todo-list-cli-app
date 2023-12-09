import click
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return file.read().splitlines()
    return []

def save_tasks(tasks_list):
    with open(TASKS_FILE, "w") as file:
        for task in tasks_list:
            file.write(task + "\n")

@click.command()
@click.option("--new_task", default=None, help="Adding new task")
@click.option("--show_task", is_flag=True, help="Showing all of your tasks")
@click.option("--delete_task", type=int, help="Delete a task by index")
def todo_list(new_task, show_task, delete_task):
    tasks_list = load_tasks()  # Load tasks from file
    
    if new_task:  # If new task has been provided through the option
        tasks_list.append(new_task)
        save_tasks(tasks_list)  # Save updated tasks
        click.echo(f"New task '{new_task}' has been created")
    
    if show_task:  # If show_task option is provided, display all tasks
        if tasks_list:
            click.echo("Your tasks:")
            for index, task in enumerate(tasks_list, start=1):
                click.echo(f"{index}. {task}")
        else:
            click.echo("No tasks available.")
    
    if delete_task is not None:  # If delete_task option is provided
        deleted_task = tasks_list.pop(delete_task - 1)  # Remove task based on index
        save_tasks(tasks_list)  # Save updated tasks
        click.echo(f"Task '{deleted_task}' has been deleted")
        click.echo("Invalid index. No task deleted.")

    if not any([new_task, show_task, delete_task]):
        click.echo("Please provide an option: --new_task, --show_task, or --delete_task")

if __name__ == "__main__":
    todo_list()