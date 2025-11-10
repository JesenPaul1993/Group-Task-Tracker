# simple in-memory to-do manager
tasks = []

def add_task(task: str):
    tasks.append(task)
    return tasks

def view_tasks():
    return list(tasks)

def remove_task(task: str):
    if task in tasks:
        tasks.remove(task)
        return True
    return False
