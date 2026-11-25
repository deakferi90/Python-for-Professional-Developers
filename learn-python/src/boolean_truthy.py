status = "in_progress"


def is_task_done(status):
    return status == "done"


if status == "done":
    print("Task is done")

elif status == "in_progress":
    print("Task is in progress")
else:
    print("Task is not done")
