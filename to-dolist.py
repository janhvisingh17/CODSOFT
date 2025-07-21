
import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯To-Do List")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f8ff")  # Light blue background

        self.tasks = load_tasks()

        self.task_var = tk.StringVar()

        # Task Entry
        self.entry = tk.Entry(root, textvariable=self.task_var, width=30, font=("Arial", 12))
        self.entry.pack(pady=10)

        # Add Button
        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task,
                                 bg="#4caf50", fg="white", font=("Arial", 10, "bold"))
        self.add_btn.pack(pady=5)

        # Listbox for tasks
        self.listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12),
                                  bg="#fff8dc", fg="black", selectbackground="#87cefa")
        self.listbox.pack(pady=10)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg="#f0f8ff")
        self.button_frame.pack()

        # Complete Button
        self.complete_btn = tk.Button(self.button_frame, text="Completed", command=self.complete_task,
                                      bg="#2196f3", fg="white", font=("Arial", 10))
        self.complete_btn.grid(row=0, column=0, padx=10)

        # Delete Button
        self.delete_btn = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task,
                                    bg="#f44336", fg="white", font=("Arial", 10))
        self.delete_btn.grid(row=0, column=1, padx=10)

        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✅" if task["done"] else "❌"
            display_text = f"{task['task']} [{status}]"
            self.listbox.insert(tk.END, display_text)

    def add_task(self):
        task_text = self.task_var.get().strip()
        if task_text:
            self.tasks.append({"task": task_text, "done": False})
            self.task_var.set("")
            self.update_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def complete_task(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            self.tasks[idx]["done"] = True
            self.update_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showinfo("Selection Needed", "Select a task to mark complete.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            del self.tasks[idx]
            self.update_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showinfo("Selection Needed", "Select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
