import tkinter as tk
from tkinter import messagebox


# ---------------- DATA ----------------

projects = []
tasks = []
comments = []


# ---------------- FUNCTIONS ----------------

def add_project():
    name = project_entry.get().strip()

    if name == "":
        messagebox.showwarning("Warning", "Please enter a project name.")
        return

    projects.append(name)
    project_list.insert(tk.END, name)

    project_entry.delete(0, tk.END)


def add_task():
    title = task_entry.get().strip()
    assigned = user_entry.get().strip()

    if title == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return

    if assigned == "":
        assigned = "Not assigned"

    task = title + " | Assigned to: " + assigned

    tasks.append(task)
    task_list.insert(tk.END, "⏳ " + task)

    task_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)


def complete_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a task first."
        )
        return

    index = selected[0]
    task = tasks[index]

    task_list.delete(index)
    task_list.insert(index, "✅ " + task)


def add_comment():
    text = comment_entry.get().strip()

    if text == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a comment."
        )
        return

    comments.append(text)
    comment_list.insert(
        tk.END,
        "💬 " + text
    )

    comment_entry.delete(0, tk.END)


def delete_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a task first."
        )
        return

    index = selected[0]

    task_list.delete(index)
    tasks.pop(index)


# ---------------- WINDOW ----------------

window = tk.Tk()

window.title("Project Management Tool")

window.geometry("700x750")

window.resizable(False, False)


# ---------------- TITLE ----------------

title = tk.Label(
    window,
    text="PROJECT MANAGEMENT TOOL",
    font=("Arial", 22, "bold")
)

title.pack(pady=15)


# ---------------- PROJECT ----------------

tk.Label(
    window,
    text="1. CREATE PROJECT",
    font=("Arial", 14, "bold")
).pack()

project_entry = tk.Entry(
    window,
    width=50
)

project_entry.pack(pady=5)

tk.Button(
    window,
    text="Create Project",
    width=20,
    command=add_project
).pack()

project_list = tk.Listbox(
    window,
    width=65,
    height=4
)

project_list.pack(pady=10)


# ---------------- TASK ----------------

tk.Label(
    window,
    text="2. CREATE & ASSIGN TASK",
    font=("Arial", 14, "bold")
).pack()

task_entry = tk.Entry(
    window,
    width=50
)

task_entry.pack(pady=5)

task_entry.insert(
    0,
    "Enter task"
)

user_entry = tk.Entry(
    window,
    width=50
)

user_entry.pack(pady=5)

user_entry.insert(
    0,
    "Enter assigned user"
)

tk.Button(
    window,
    text="Create Task",
    width=20,
    command=add_task
).pack()

task_list = tk.Listbox(
    window,
    width=80,
    height=7
)

task_list.pack(pady=10)


# ---------------- TASK BUTTONS ----------------

button_frame = tk.Frame(window)

button_frame.pack()

tk.Button(
    button_frame,
    text="Complete Task",
    width=18,
    command=complete_task
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Delete Task",
    width=18,
    command=delete_task
).grid(row=0, column=1, padx=5)


# ---------------- COMMENTS ----------------

tk.Label(
    window,
    text="3. TASK COMMENTS",
    font=("Arial", 14, "bold")
).pack(pady=15)

comment_entry = tk.Entry(
    window,
    width=50
)

comment_entry.pack(pady=5)

tk.Button(
    window,
    text="Add Comment",
    width=20,
    command=add_comment
).pack()

comment_list = tk.Listbox(
    window,
    width=65,
    height=5
)

comment_list.pack(pady=10)


# ---------------- START PROGRAM ----------------

window.mainloop()
