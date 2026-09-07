disaster_reports = {}

while True:
  print("\n1. Report Disaster | 2. View Reports | 3. Delete Report | 4. Exit")
  choice = input("Choose an option: ")

  if choice == "1":
    r_id = input("Enter Report ID: ")
    loc = input("Enter Location: ")
    typ = input("Enter Type (e.g., Fire): ")
    disaster_reports[r_id] = f"Type: {typ}, Location: {loc}"
    print("Report saved successfully.")

  elif choice == "2":
    for r_id, details in disaster_reports.items():
      print(f"ID: {r_id} -> {details}")

  elif choice == "3":
    r_id = input("Enter Report ID to delete: ")
    if r_id in disaster_reports:
      del disaster_reports[r_id]
      print("Report deleted.")
    else:
      print("ID not found.")

  elif choice == "4":
    print("Exiting.")
    break
