# Default arguments in Python are evaluated once when the function is defined,
# not each time it is called. Using a mutable object like a list ([]) as a default
# argument causes all function calls without a provided list to share and modify
# the exact same list instance in memory.

def add_task(task_name, task_list=[]):
    task_list.append(task_name)
    return task_list


print(add_task("Buy groceries"))
print(add_task("Clean room"))
print(add_task("Read book"))