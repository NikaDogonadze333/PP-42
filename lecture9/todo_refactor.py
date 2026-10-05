def add_task(task_name, task_list=None):
    if task_list is None:
        task_list = []
    task_list.append(task_name)
    return task_list


print(add_task("Buy groceries"))
print(add_task("Clean room"))
print(add_task("Read book"))