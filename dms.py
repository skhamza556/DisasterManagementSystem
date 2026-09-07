import tkinter as tk
from tkinter import messagebox, ttk

# Storage dictionary
disaster_reports = {}


# --- CORE FUNCTIONS ---
def add_report():
  r_id = id_entry.get().strip()
  loc = loc_entry.get().strip()
  typ = typ_entry.get().strip()
  sev = sev_combobox.get()

  if not r_id or not loc or not typ:
    messagebox.showerror("Error", "All fields are required!")
    return

  if r_id in disaster_reports:
    messagebox.showerror("Error", "Report ID already exists!")
    return

  # Save data
  disaster_reports[r_id] = (typ, loc, sev)

  # Clear inputs
  id_entry.delete(0, tk.END)
  loc_entry.delete(0, tk.END)
  typ_entry.delete(0, tk.END)

  update_table()
  messagebox.showinfo("Success", "Report added successfully!")


def delete_report():
  selected_item = tree.selection()
  if not selected_item:
    messagebox.showwarning("Warning", "Please select a report to delete.")
    return

  # Get the Report ID from the selected row
  r_id = tree.item(selected_item)['values'][0]

  if str(r_id) in disaster_reports:
    del disaster_reports[str(r_id)]
    update_table()
    messagebox.showinfo("Deleted", f"Report {r_id} removed.")


def update_table():
  # Clear existing rows in the table
  for row in tree.get_children():
    tree.delete(row)

  # Repopulate table
  for r_id, (typ, loc, sev) in disaster_reports.items():
    tree.insert("", tk.END, values=(r_id, typ, loc, sev))


# --- GUI SETUP ---
root = tk.Tk()
root.title("Disaster Management System v2.0")
root.geometry("600x450")

# Input Form Frame
form_frame = tk.LabelFrame(root, text="Report New Disaster", padx=10, pady=10)
form_frame.pack(fill="x", padx=10, pady=5)

tk.Label(form_frame, text="Report ID:").grid(row=0, column=0, sticky="w")
id_entry = tk.Entry(form_frame)
id_entry.grid(row=0, column=1, padx=5, pady=2)

tk.Label(form_frame, text="Location:").grid(row=1, column=0, sticky="w")
loc_entry = tk.Entry(form_frame)
loc_entry.grid(row=1, column=1, padx=5, pady=2)

tk.Label(form_frame, text="Type (e.g. Fire):").grid(row=0, column=2, sticky="w")
typ_entry = tk.Entry(form_frame)
typ_entry.grid(row=0, column=3, padx=5, pady=2)

tk.Label(form_frame, text="Severity:").grid(row=1, column=2, sticky="w")
sev_combobox = ttk.Combobox(form_frame, values=["Low", "Medium", "High"])
sev_combobox.current(0)
sev_combobox.grid(row=1, column=3, padx=5, pady=2)

add_btn = tk.Button(
    form_frame, text="Submit Report", command=add_report, bg="green", fg="white"
)
add_btn.grid(row=2, column=0, columnspan=4, pady=10, sticky="ew")

# Data Table Frame
table_frame = tk.LabelFrame(root, text="Active Complaints", padx=10, pady=10)
table_frame.pack(fill="both", expand=True, padx=10, pady=5)

columns = ("id", "type", "location", "severity")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")
tree.heading("id", text="ID")
tree.heading("type", text="Type")
tree.heading("location", text="Location")
tree.heading("severity", text="Severity")

# Adjust column widths
for col in columns:
  tree.column(col, width=100, anchor="center")
tree.pack(fill="both", expand=True, side="left")

# Delete Button
del_btn = tk.Button(
    root,
    text="Delete Selected Report",
    command=delete_report,
    bg="red",
    fg="white",
)
del_btn.pack(fill="x", padx=10, pady=10)

root.mainloop()
